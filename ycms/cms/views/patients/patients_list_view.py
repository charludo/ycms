import logging

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from ...decorators import permission_required
from ...forms import PatientForm
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
        return {
            "patients": Patient.objects.all().order_by("-created_at"),
            **super().get_context_data(**kwargs),
        }

    def post(self, request, *args, **kwargs):
        r"""
        :param request: The current request
        :type request: ~django.http.HttpRequest

        :param \*args: The supplied arguments
        :type \*args: list

        :param \**kwargs: The supplied keyword arguments
        :type \**kwargs: dict

        :return: Redirect to list of patients
        :rtype: ~django.http.HttpResponseRedirect
        """

        if (method := request.POST["_method"]) == "DELETE":
            patient = get_object_or_404(Patient, id=request.POST["id"])

            patient.delete()

            messages.success(
                request,
                _('Patient "{} {}" has been deleted.').format(
                    patient.first_name, patient.last_name
                ),
            )

        else:
            data = request.POST.copy()
            name = data["name"].split(", ")

            if len(name) != 2:
                messages.error(
                    request, _('Name: Wrong syntax. Use "Lastname, Firstname".')
                )
                return redirect("cms:protected:patients")

            data["first_name"] = name[1]
            data["last_name"] = name[0]
            data.pop("name")
            data["insurance_type"] = "insurance_type" in data

            if method == "PUT":
                patient_form = PatientForm(
                    data=data, additional_instance_attributes={"creator": request.user}
                )

                if not patient_form.is_valid():
                    patient_form.add_error_messages(request)
                    return render(
                        request,
                        self.template_name,
                        self.get_context_data(**kwargs)
                        | {"patient_form": patient_form},
                    )

                patient = patient_form.save()

                messages.success(
                    request,
                    _('Patient "{} {}" has been created.').format(
                        patient.first_name, patient.last_name
                    ),
                )

            elif method == "POST":
                patient = Patient.objects.get(id=data["id"])
                patient_form = PatientForm(instance=patient, data=data)

                if not patient_form.is_valid():
                    patient_form.add_error_messages(request)
                    return render(
                        request,
                        self.template_name,
                        self.get_context_data(**kwargs)
                        | {"patient_form": patient_form},
                    )

                patient = patient_form.save()

                messages.success(
                    request,
                    _('Patient "{} {}" has been edited.').format(
                        patient.first_name, patient.last_name
                    ),
                )

        return redirect("cms:protected:patients")
