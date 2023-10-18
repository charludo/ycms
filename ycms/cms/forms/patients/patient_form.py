import logging

from django import forms

from ...models import Patient
from ..custom_model_form import CustomModelForm

logger = logging.getLogger(__name__)


class PatientForm(CustomModelForm):
    """
    Form for creating patients
    """

    class Meta:
        """
        This class contains additional meta configuration of the form class, see the :class:`django.forms.ModelForm`
        for more information.
        """

        model = Patient
        fields = ["first_name", "last_name", "private_patient", "diagnosis_code"]
        widgets = {"private_patient": forms.RadioSelect()}
