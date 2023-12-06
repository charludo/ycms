from django.db import models
from django.shortcuts import redirect
from django.views.generic import TemplateView

from ...constants import gender
from ...forms import IntakeBedAssignmentForm, PatientForm
from ...models import BedAssignment, Ward
from ...models.timetravel_manager import current_or_travelled_time


class WardView(TemplateView):
    """
    View to see a ward
    """

    model = Ward
    template_name = "ward/ward.html"
    context_object_name = "ward"

    def get_context_data(self, pk=None, **kwargs):
        """
        This function returns a list of all rooms in the ward

        :param pk: The ID of the ward that should be shown
        :type pk: int or None

        :param kwargs: The supplied keyword arguments
        :type kwargs: dict

        :return: Response for filtered offers
        :rtype: ~django.template.response.TemplateResponse
        """
        if not pk and self.request.user.assigned_ward:
            pk = self.request.user.assigned_ward.id
        elif not pk:
            pk = 1
        ward = Ward.objects.get(id=pk)
        rooms = [
            (
                room,
                [
                    (
                        patient,
                        PatientForm(instance=patient),
                        IntakeBedAssignmentForm(instance=patient.current_stay),
                    )
                    for patient in room.patients()
                ],
            )
            for room in ward.rooms.all()
        ]
        wards = Ward.objects.all()
        unassigned_bed_assignments = [
            (
                unassigned,
                PatientForm(instance=unassigned.medical_record.patient),
                IntakeBedAssignmentForm(instance=unassigned),
            )
            for unassigned in BedAssignment.objects.filter(
                models.Q(admission_date__lte=current_or_travelled_time())
                & models.Q(bed__isnull=True)
                & (
                    models.Q(discharge_date__gt=current_or_travelled_time())
                    | models.Q(discharge_date__isnull=True)
                )
                & (
                    models.Q(recommended_ward__isnull=True)
                    | models.Q(recommended_ward=ward)
                )
            )
        ]

        return {
            "rooms": rooms,
            "corridor_index": len(rooms) // 2,
            "ward": ward,
            "patient_info": self._get_patient_info(ward.patients),
            "wards": wards,
            "selected_ward_id": pk,
            "unassigned_bed_assignments": unassigned_bed_assignments,
            **super().get_context_data(**kwargs),
        }

    def _get_patient_info(self, patients):
        patient_info = {}
        patient_info["total_patients"] = patients.count
        patient_info["female_patients"] = patients.filter(gender=gender.FEMALE).count
        patient_info["male_patients"] = patients.filter(gender=gender.MALE).count
        return patient_info

    def post(self, request, *args, **kwargs):
        """
        This function handles the post request for ward view
        """
        if selected_ward_id := request.POST.get("ward"):
            return redirect("cms:protected:ward_detail", pk=selected_ward_id)
        return redirect("cms:protected:index")
