from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from ..constants import insurance_types
from .abstract_base_model import AbstractBaseModel
from .patient import Patient
from .user import User
from .ward import Ward


class Room(AbstractBaseModel):
    """
    Data model representing a Room.
    """

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    room_number = models.CharField(
        max_length=32,
        verbose_name=_("room number"),
        help_text=_("number of this room within its ward"),
    )
    ward = models.ForeignKey(
        Ward,
        on_delete=models.CASCADE,
        verbose_name=_("ward"),
        help_text=_("The ward this room belongs to"),
    )

    @cached_property
    def total_beds(self):
        """
        Helper property for accessing the rooms bed count

        :return: number of beds in the room
        :rtype: int
        """
        return self.beds.count()

    @cached_property
    def available_beds(self):
        """
        Helper property for accessing the rooms free bed count

        :return: number of free beds in the room
        :rtype: int
        """
        return self.beds.filter(is_available=True).count()

    @cached_property
    def patients(self):
        """
        Helper property for accessing all patients currently stationed in the room

        :return: patients in the room
        :rtype: list [ ~ycms.cms.models.patient.Patient ]
        """
        return Patient.objects.filter(bedassignment__bed__room=self).distinct()

    @cached_property
    def is_private(self):
        """
        Helper property for determining if the room should be considered private

        :return: whether this is a private room
        :rtype: boolean
        """
        return self.patients.filter(
            current_stay__patient__insurance_type=insurance_types.PRIVATE
        ).exists()

    def __str__(self):
        """
        This overwrites the default Django :meth:`~django.db.models.Model.__str__` method which would return ``Room object (id)``.
        It is used in the Django admin backend and as label for ModelChoiceFields.

        :return: A readable string representation of the room
        :rtype: str
        """
        return f"Room {self.room_number} in Ward {self.ward.ward_number}"

    def get_repr(self):
        """
        This overwrites the default Django ``__repr__()`` method which would return ``<Room: Room object (id)>``.
        It is used for logging.

        :return: The canonical string representation of the room
        :rtype: str
        """
        return f"<Room (number: {self.ward_number}, ward: {self.ward.ward_number})>"

    class Meta:
        verbose_name = _("room")
        verbose_name_plural = _("rooms")