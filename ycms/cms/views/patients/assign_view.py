import json
import logging

from django.http import JsonResponse
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
        bed_assignment = BedAssignment.objects.get(id=assignment_id)

        return {
            "bed_assignment": bed_assignment,
            "rooms": rooms,
            "corridor_index": str(len(rooms) // 2),
            "ward": ward,
            "wards": wards,
            **super().get_context_data(**kwargs),
        }

    def post(self, request, *args, **kwargs):
        """
        This function assign a patient to a room
        """
        data = json.loads(request.body)
        bed_id = data.get("bed_id")
        bed_assignment = BedAssignment.objects.get(pk=kwargs["assignment_id"])
        bed = Bed.objects.get(pk=bed_id)

        bed_assignment.bed = bed
        bed_assignment.save()

        return JsonResponse({"success": True})
