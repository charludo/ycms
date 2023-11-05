import logging

from django import forms
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ..models import BedAssignment
from .custom_model_form import CustomModelForm

logger = logging.getLogger(__name__)


class IntakeBedAssignmentForm(CustomModelForm):
    """
    Form for creating intake bed assignments. Not used for assignment by station managers.
    """

    class Meta:
        """
        This class contains additional meta configuration of the form class, see the :class:`django.forms.ModelForm`
        for more information.
        """

        model = BedAssignment
        fields = ["admission_date", "recommended_ward", "accompanied"]
        widgets = {
            "admission_date": forms.NumberInput(
                attrs={"type": "date", "value": timezone.now().date}
            )
        }

    def save(self, commit=True):
        """
        This method extends the default ``save()``-method of the base :class:`~django.forms.ModelForm`
        to create a new bed assignment.

        :param commit: Whether or not the changes should be written to the database
        :type commit: bool

        :return: The saved medical record
        :rtype: ~ycms.cms.models.medical_record.MedicalRecord
        """
        cleaned_data = self.cleaned_data
        new_record = BedAssignment.objects.create(
            creator=self.instance.creator,
            medical_record=self.instance.medical_record,
            admission_date=cleaned_data["admission_date"],
            recommended_ward=cleaned_data["recommended_ward"],
            accompanied=cleaned_data["accompanied"],
        )
        return new_record
