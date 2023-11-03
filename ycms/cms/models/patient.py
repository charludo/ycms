from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from ..constants import gender, insurance_types
from .abstract_base_model import AbstractBaseModel
from .user import User


class Patient(AbstractBaseModel):
    """
    Data model representing a Patient.
    """

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    insurance_type = models.BooleanField(
        verbose_name=_("insurance type"),
        help_text=_("Whether the patient is privately insured or not"),
        choices=insurance_types.CHOICES,
        default=insurance_types.STATUTORY,
    )
    first_name = models.CharField(
        max_length=32,
        verbose_name=_("first name"),
        help_text=_("First name of the patient"),
    )
    last_name = models.CharField(
        max_length=64,
        verbose_name=_("last name"),
        help_text=_("Last name of the patient"),
    )
    gender = models.CharField(
        max_length=1,
        choices=gender.CHOICES,
        verbose_name=_("gender"),
        help_text=_("Gender of the patient"),
    )
    date_of_birth = models.DateField(
        verbose_name=_("date of birth"), help_text=_("Date of birth of the patient")
    )

    @cached_property
    def current_stay(self):
        """
        Helper property for accessing the patient's current hospital stay

        :return: the current bed assignment
        :rtype: ~ycms.cms.models.bed_assignment.BedAssignment
        """
        return self.bed_assignment.latest("created_at")

    @cached_property
    def current_bed(self):
        """
        Helper property for accessing the patient's current bed

        :return: the current bed
        :rtype: ~ycms.cms.models.bed.Bed
        """
        return self.current_stay.bed if self.current_stay else None

    @cached_property
    def current_room(self):
        """
        Helper property for accessing the patient's current room

        :return: the current room
        :rtype: ~ycms.cms.models.room.Room
        """
        return self.current_bed.room if self.current_bed else None

    @cached_property
    def current_ward(self):
        """
        Helper property for accessing the patient's current ward

        :return: the current ward
        :rtype: ~ycms.cms.models.ward.Ward
        """
        return self.current_room.ward if self.current_room else None

    def __str__(self):
        """
        This overwrites the default Django :meth:`~django.db.models.Model.__str__` method which would return ``Patient object (id)``.
        It is used in the Django admin backend and as label for ModelChoiceFields.

        :return: A readable string representation of the patient
        :rtype: str
        """
        return f"{self.last_name}, {self.first_name} (patient {self.id})"

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