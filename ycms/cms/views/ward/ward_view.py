from django.db import models
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from ...constants import gender
from ...decorators import permission_required
from ...forms import IntakeBedAssignmentForm, PatientForm
from ...models import BedAssignment, Ward
from ...models.timetravel_manager import current_or_travelled_time


@method_decorator(permission_required("cms.change_patient"), name="dispatch")
class WardView(TemplateView):
    """
    View to see a ward
    """

    model = Ward
    template_name = "ward/ward.html"
    context_object_name = "ward"

    def get(self, request, *args, pk=None, **kwargs):
        """
        Helper function for redirecting in case the user requested the ward timeline
        """
        if not pk and self.request.user.assigned_ward:
            pk = self.request.user.assigned_ward.id
        elif not pk:
            pk = 3 if Ward.objects.get(pk=3) else 1

        if self.request.user.ward_as_timeline:
            return redirect("cms:protected:timeline", pk=pk)
        return super().get(request, *args, pk=pk, **kwargs)

    def get_context_data(self, **kwargs):
        """
        This function returns a list of all rooms in the ward

        :param kwargs: The supplied keyword arguments
        :type kwargs: dict

        :return: Response for filtered offers
        :rtype: ~django.template.response.TemplateResponse
        """
        pk = kwargs.get("pk")
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
            ).order_by("-updated_at")
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
