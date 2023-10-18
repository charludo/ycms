from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ...constants import insurance_types
from ..abstract_base_model import AbstractBaseModel
from ..users.user import User


class Patient(AbstractBaseModel):
    """
    Data model representing a Patient.
    """

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, null=False)
    first_name = models.CharField(
        max_length=255,
        verbose_name=_("first name"),
        help_text=_("First name of the patient"),
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name=_("last name"),
        help_text=_("Surname of the patient"),
    )
    private_patient = models.BooleanField(
        verbose_name=_("insurance type"),
        help_text=_("Whether the patient is privately insured or not"),
        choices=insurance_types.CHOICES,
        default=insurance_types.STATUTORY,
    )
    diagnosis_code = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_("diagnosis code"),
        help_text=_("Diagnosis code according to ICD10-2019"),
    )

    def __str__(self):
        """
        This overwrites the default Django :meth:`~django.db.models.Model.__str__` method which would return ``Patient object (id)``.
        It is used in the Django admin backend and as label for ModelChoiceFields.

        :return: A readable string representation of the patient
        :rtype: str
        """
        return f"Patient {self.id}"

    def get_repr(self):
        """
        This overwrites the default Django ``__repr__()`` method which would return ``<Patient: Patient object (id)>``.
        It is used for logging.

        :return: The canonical string representation of the patient
        :rtype: str
        """
        return f"<Patient (id: {self.id})>"

    class Meta:
        verbose_name = _("patient")
        verbose_name_plural = _("patients")
