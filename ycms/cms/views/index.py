import logging

from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
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
        Submit :class:`~ycms.cms.forms.patients.patient_form.PatientForm`

        :param request: The current request
        :type request: ~django.http.HttpRequest

        :param \*args: The supplied arguments
        :type \*args: list

        :param \**kwargs: The supplied keyword arguments
        :type \**kwargs: dict

        :raises ~django.core.exceptions.PermissionDenied: If user does not have the permission to edit the specific page

        :return: Redirect to list of patients
        :rtype: ~django.http.HttpResponseRedirect
        """
        if not request.user.is_authenticated:
            # Note: this is just for demonstration purposes. Usually, you would have
            # a ListView for the existing patients, and a separate CreateView for creating
            # them. Then the redirecting is handled by the AccessControlMiddleware in
            # ~ycms.core.middleware.access_control_middleware
            return redirect_to_login(request.path)

        if not request.user.has_perm("cms.add_patient"):
            raise PermissionDenied()

        form = PatientForm(
            data=request.POST, additional_instance_attributes={"creator": request.user}
        )
        if not form.is_valid():
            form.add_error_messages(request)
            return render(
                request,
                self.template_name,
                {
                    "form": form,
                    "patients": Patient.objects.all(),
                    **self.get_context_data(**kwargs),
                },
            )

        patient = form.save()
        messages.success(
            request,
            _('Patient "{} {}" has been saved with diagnosis "{}".').format(
                patient.first_name, patient.last_name, patient.diagnosis_code
            ),
        )
        return redirect("cms:public:index")
