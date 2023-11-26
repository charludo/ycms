import logging

from django import forms
from django.utils import timezone

from ...models import BedAssignment
from ..custom_model_form import CustomModelForm

logger = logging.getLogger(__name__)


class BedAssignmentForm(CustomModelForm):
    """
    Form for creating bed assignments.
    """

    class Meta:
        """
        This class contains additional meta configuration of the form class, see the :class:`django.forms.ModelForm`
        for more information.
        """

        model = BedAssignment
        fields = ["medical_record", "admission_date", "discharge_date"]
        widgets = {
            "medical_record": forms.HiddenInput(),
            "admission_date": forms.NumberInput(
                attrs={"type": "date", "value": timezone.now().date}
            ),
            "discharge_date": forms.NumberInput(
                attrs={
                    "type": "date",
                    "value": (timezone.now() + timezone.timedelta(days=1)).date,
                }
            ),
        }

