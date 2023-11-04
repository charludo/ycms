import datetime

from django.http import JsonResponse
from django.views.generic import View

from ...models import BedAssignment


class DischargePatientView(View):
    """
    View to discharge a patient
    """

    def post(self, request, *args, **kwargs):
        """
        This function discharges a patient
        """
        bed_assignment = BedAssignment.objects.get(pk=kwargs["assignment_id"])
        bed_assignment.discharge_date = datetime.datetime.now()
        bed_assignment.save()

        return JsonResponse({"success": True})
