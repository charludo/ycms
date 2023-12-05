import datetime

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import View

from ...decorators import permission_required
from ...models import BedAssignment


@method_decorator(permission_required("cms.add_patient"), name="dispatch")
class DischargePatientView(View):
    """
    View to discharge a patient
    """

    def post(self, request, *args, **kwargs):
        """
        This function discharges a patient
        """
        bed_assignment = BedAssignment.objects.get(pk=kwargs["assignment_id"])
        bed_assignment.discharge_date = (
            datetime.datetime.now()
            if not (date := request.POST.get("new_date"))
            else date
        )
        bed_assignment.save()

        return JsonResponse({"success": True})
