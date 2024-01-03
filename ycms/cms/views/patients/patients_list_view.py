import logging

from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

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
            "patients": [
                (patient, PatientForm(instance=patient, prefix=patient.id))
                for patient in Patient.objects.all().order_by("-created_at")
            ],
            "new_patient_form": PatientForm(),
            **super().get_context_data(**kwargs),
        }


@method_decorator(permission_required("cms.add_patient"), name="dispatch")
class PatientCreateView(CreateView):
    """
    View to create a patient
    """

    model = Patient
    success_url = reverse_lazy("cms:protected:patients")
    form_class = PatientForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(
            self.request,
            _("Patient {}, {} has been created.").format(
                form.instance.last_name, form.instance.first_name
            ),
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        form.add_error_messages(self.request)
        return redirect("cms:protected:patients")


@method_decorator(permission_required("cms.add_patient"), name="dispatch")
class PatientUpdateView(UpdateView):
    """
    View to update a patient
    """

    model = Patient
    success_url = reverse_lazy("cms:protected:patients")
    form_class = PatientForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"prefix": self.kwargs["pk"]})
        return kwargs

    def form_valid(self, form):
        messages.success(
            self.request,
            _("Patient {}, {} has been updated.").format(
                form.instance.last_name, form.instance.first_name
            ),
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        form.add_error_messages(self.request)
        return redirect("cms:protected:patients")


@method_decorator(permission_required("cms.add_patient"), name="dispatch")
class PatientDeleteView(DeleteView):
    """
    View to delete a patient
    """

    model = Patient
    success_url = reverse_lazy("cms:protected:patients")

    def form_valid(self, form):
        messages.success(self.request, _("Patient has been deleted."))
        return super().form_valid(form)

    def form_invalid(self, form):
        form.add_error_messages(self.request)
        return redirect("cms:protected:patients")
