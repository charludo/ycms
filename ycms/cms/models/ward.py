from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from .abstract_base_model import AbstractBaseModel
from .patient import Patient
from .user import User


class Ward(AbstractBaseModel):
    """
    Data model representing a Ward.
    """

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    ward_number = models.CharField(
        unique=True,
        max_length=32,
        verbose_name=_("ward number"),
        help_text=_("Number of the ward"),
    )
    floor = models.IntegerField(
        verbose_name=_("floor"),
        help_text=_("Floor on which the nurse station for this ward is located"),
    )
    name = models.CharField(
        max_length=32,
        verbose_name=_("ward name"),
        help_text=_("Name this ward is commonly referred to by"),
    )

    @cached_property
    def total_beds(self):
        """
        Helper property for accessing the wards bed count

        :return: number of beds in the ward
        :rtype: int
        """
        return sum(room.total_beds for room in self.rooms.all())

    @cached_property
    def available_beds(self):
        """
        Helper property for accessing the wards free bed count

        :return: number of free beds in the ward
        :rtype: int
        """
        return sum(room.available_beds for room in self.rooms.all())

    @cached_property
    def patients(self):
        """
        Helper property for accessing all patients currently stationed in the ward

        :return: patients in the ward
        :rtype: list [ ~ycms.cms.models.patient.Patient ]
        """
        return Patient.objects.filter(bedassignment__bed__room__ward=self).distinct()

    def __str__(self):
        """
        This overwrites the default Django :meth:`~django.db.models.Model.__str__` method which would return ``Ward object (id)``.
        It is used in the Django admin backend and as label for ModelChoiceFields.

        :return: A readable string representation of the ward
        :rtype: str
        """
        return f"{self.name} (ward {self.ward_number})"

    def get_repr(self):
        """
        This overwrites the default Django ``__repr__()`` method which would return ``<Ward: Ward object (id)>``.
        It is used for logging.

        :return: The canonical string representation of the ward
        :rtype: str
        """
        return f"<Ward (number: {self.ward_number})>"

    class Meta:
        verbose_name = _("ward")
        verbose_name_plural = _("wards")
