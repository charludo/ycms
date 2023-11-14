import logging

from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from ...decorators import permission_required
from ...models import Patient

logger = logging.getLogger(__name__)


@method_decorator(permission_required("cms.view_patient"), name="dispatch")
class PatientsListView(TemplateView):
    """
    View to see all patients and add a new one
    """

    template_name = "patients_list.html"

    def get_context_data(self, **kwargs):
        """
        This function returns a list of all patients.

        :param kwargs: The supplied keyword arguments
        :type kwargs: dict

        :return: Response for filtered offers
        :rtype: ~django.template.response.TemplateResponse
        """
        return {"patients": Patient.objects.all(), **super().get_context_data(**kwargs)}
