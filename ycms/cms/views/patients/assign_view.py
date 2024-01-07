import logging

from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from ...models import Bed, BedAssignment, Ward

logger = logging.getLogger(__name__)


class AssignPatientView(TemplateView):
    """
    View allowing to assign the bed assignment visually
    """

    model = BedAssignment
    template_name = "bed_assignment/assign_bed_assignment.html"
    context_object_name = "bed_assignment"

    def get_context_data(self, **kwargs):
        ward_id = self.kwargs["ward_id"]
        assignment_id = self.kwargs["assignment_id"]

        ward = Ward.objects.get(id=ward_id)
        rooms = ward.rooms.all()
        wards = Ward.objects.all()
        bed_assignment = get_object_or_404(BedAssignment, id=assignment_id)

        return {
            "bed_assignment": bed_assignment,
            "rooms": rooms,
            "corridor_index": len(rooms) // 2,
            "ward": ward,
            "wards": wards,
            **super().get_context_data(**kwargs),
        }

    def post(self, request, *args, **kwargs):
        """
        This function assigns a patient to a room
        """
        assignment_id = kwargs["assignment_id"]
        bed_assignment = get_object_or_404(BedAssignment, pk=assignment_id)

        bed_id = request.POST.get("bed_id")
        try:
            bed_assignment.bed = Bed.objects.get(pk=bed_id)
        except Bed.DoesNotExist:
            bed_assignment.bed = None

        if new_ward_id := request.POST.get("new_ward"):
            bed_assignment.recommended_ward = get_object_or_404(Ward, pk=new_ward_id)

        bed_assignment.save()
        return redirect("cms:protected:ward_detail", pk=kwargs["ward_id"])
