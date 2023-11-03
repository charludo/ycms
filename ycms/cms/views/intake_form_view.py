import logging

from django.contrib import messages
from django.db import transaction
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from ..decorators import permission_required
from ..forms import IntakeBedAssignmentForm, IntakeRecordForm, PatientForm
from ..models import Patient

logger = logging.getLogger(__name__)


@method_decorator(permission_required("cms.add_patient"), name="dispatch")
class IntakeFormView(TemplateView):
    """
    View to perform intake on new or existing patients
    """

    template_name = "intake_form.html"

    def get_context_data(self, **kwargs):
        """
        This function returns a list of all patients,
        as well as a form for creating a new one

        :param kwargs: The supplied keyword arguments
        :type kwargs: dict

        :return: Response for filtered offers
        :rtype: ~django.template.response.TemplateResponse
        """
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "patient_form": PatientForm(),
                "record_form": IntakeRecordForm(),
                "bed_form": IntakeBedAssignmentForm(),
            }
        )
        return context

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

        :return: Redirect to list of patients
        :rtype: ~django.http.HttpResponseRedirect
        """
        # Get the existing patient or create a new one
        if patient_id := request.POST.get("patient"):
            patient = Patient.objects.get(id=patient_id)
            patient_form = PatientForm()
        else:
            patient_form = PatientForm(
                data=request.POST,
                additional_instance_attributes={"creator": request.user},
            )
            if not patient_form.is_valid():
                patient_form.add_error_messages(request)
                return render(
                    request,
                    self.template_name,
                    self.get_context_data(**kwargs) | {"patient_form": patient_form},
                )

            patient = patient_form.save()

            messages.success(
                request,
                _('Patient "{} {}" has been saved.').format(
                    patient.first_name, patient.last_name
                ),
            )

        # Create a new medical record for the patient
        record_form = IntakeRecordForm(
            data=request.POST,
            additional_instance_attributes={
                "creator": request.user,
                "selected_patient": patient,
            },
        )

        if not record_form.is_valid():
            record_form.add_error_messages(request)
            return render(
                request,
                self.template_name,
                self.get_context_data(**kwargs)
                | {"patient_form": patient_form, "record_form": record_form},
            )

        record = record_form.save()

        # Create a new bed assignment for the medical record
        bed_form = IntakeBedAssignmentForm(
            data=request.POST,
            additional_instance_attributes={
                "creator": request.user,
                "medical_record": record,
            },
        )

        if not bed_form.is_valid():
            bed_form.add_error_messages(request)
            return render(
                request,
                self.template_name,
                self.get_context_data(**kwargs)
                | {
                    "patient_form": patient_form,
                    "record_form": record_form,
                    "bed_form": bed_form,
                },
            )

        bed_form.save()

        messages.success(
            request,
            _('Intake for patient "{} {}" with diagnosis "{}" has been saved.').format(
                patient.first_name, patient.last_name, record.diagnosis_code
            ),
        )

        return redirect("cms:protected:index")
