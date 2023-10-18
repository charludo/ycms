import logging

from django.contrib import messages
from django.db import transaction
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from ..forms import PatientForm
from ..models import Patient

logger = logging.getLogger(__name__)


class IndexView(TemplateView):
    """
    View to see all patients and add a new one
    """

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        """
        This function returns a list of all patients,
        as well as a form for creating a new one

        :param request: The current request
        :type request: ~django.http.HttpRequest

        :param args: The supplied arguments
        :type args: list

        :param kwargs: The supplied keyword arguments
        :type kwargs: dict

        :return: Response for filtered offers
        :rtype: ~django.template.response.TemplateResponse
        """
        return render(
            request,
            self.template_name,
            {
                "form": PatientForm(),
                "patients": Patient.objects.all(),
                **self.get_context_data(**kwargs),
            },
        )

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        r"""
        Submit :class:`~integreat_compass.cms.forms.patients.patient_form.PatientForm`

        :param request: The current request
        :type request: ~django.http.HttpRequest

        :param \*args: The supplied arguments
        :type \*args: list

        :param \**kwargs: The supplied keyword arguments
        :type \**kwargs: dict

        :return: Redirect to list of patients
        :rtype: ~django.http.HttpResponseRedirect
        """
        form = PatientForm(
            data=request.POST, additional_instance_attributes={"creator": request.user}
        )
        if not form.is_valid():
            form.add_error_messages(request)
        else:
            patient = form.save()
            messages.success(
                request,
                _('Patient "{} {}" has been saved with diagnosis "{}".').format(
                    patient.first_name, patient.last_name, patient.diagnosis_code
                ),
            )
        return redirect("cms:public:index")
