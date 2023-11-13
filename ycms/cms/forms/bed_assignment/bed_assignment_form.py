import logging

from django import forms
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ...models import Bed, BedAssignment, MedicalRecord
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
        fields = [
            "medical_record",
            "admission_date",
            "discharge_date",
            "accompanied",
            "recommended_ward",
            "bed",
        ]
        widgets = {
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

    def __init__(self, *args, is_update=False, **kwargs):
        """
        Initialize the form with additional filters.
        1. Only show medical records that are not already assigned to a bed.
        2. Only show beds that are available.
        """
        super().__init__(*args, **kwargs)
        self.is_update = is_update
        available_beds = [x for x in Bed.objects.all() if x.is_available]
        if is_update:
            self.fields["medical_record"].queryset = MedicalRecord.objects.filter(
                bed_assignment__isnull=True
            ) | MedicalRecord.objects.filter(pk=self.instance.medical_record.id)
            if self.instance.bed:
                available_beds.insert(0, self.instance.bed)
            self.fields["bed"].queryset = Bed.objects.filter(
                id__in=[bed.id for bed in available_beds]
            )
        else:
            self.fields["medical_record"].queryset = MedicalRecord.objects.exclude(
                bed_assignment__isnull=False
            )

            self.fields["bed"].queryset = Bed.objects.filter(
                id__in=[bed.id for bed in available_beds]
            )

    def save(self, commit=True):
        """
        This method extends the default ``save()``-method of the base :class:`~django.forms.ModelForm`
        to create or update a bed assignment.

        :param commit: Whether or not the changes should be written to the database
        :type commit: bool

        :return: The saved medical record
        :rtype: ~ycms.cms.models.bed_assignment.BedAssignment
        """
        cleaned_data = self.cleaned_data

        if self.is_update:
            bed_assignment = self.instance
            bed_assignment.admission_date = cleaned_data["admission_date"]
            bed_assignment.discharge_date = cleaned_data["discharge_date"]
            bed_assignment.accompanied = cleaned_data["accompanied"]
            bed_assignment.medical_record = cleaned_data["medical_record"]
            bed_assignment.recommended_ward = cleaned_data["recommended_ward"]
            bed_assignment.bed = cleaned_data["bed"]
        else:
            bed_assignment = BedAssignment.objects.create(
                creator=self.instance.creator,
                admission_date=cleaned_data["admission_date"],
                discharge_date=cleaned_data["discharge_date"],
                accompanied=cleaned_data["accompanied"],
                medical_record=cleaned_data["medical_record"],
                recommended_ward=cleaned_data["recommended_ward"],
                bed=cleaned_data["bed"],
            )

        if commit:
            bed_assignment.save()
        return bed_assignment
