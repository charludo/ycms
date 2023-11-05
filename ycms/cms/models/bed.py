from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ..constants import bed_types
from .abstract_base_model import AbstractBaseModel
from .room import Room
from .user import User


class Bed(AbstractBaseModel):
    """
    Data model representing a Bed.
    """

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    bed_type = models.CharField(
        max_length=10,
        choices=bed_types.CHOICES,
        verbose_name=_("bed type"),
        help_text=_("specialty bed types may be available"),
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name=_("is available"),
        help_text=_("current availability status of the bed"),
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        verbose_name=_("room"),
        help_text=_("The room this bed belongs to"),
    )

    def __str__(self):
        """
        This overwrites the default Django :meth:`~django.db.models.Model.__str__` method which would return ``Bed object (id)``.
        It is used in the Django admin backend and as label for ModelChoiceFields.

        :return: A readable string representation of the bed
        :rtype: str
        """
        return f"{self.bed_type} Bed (Nr. {self.id}, Room {self.room.room_number}, Ward {self.room.ward.ward_number})"

    def get_repr(self):
        """
        This overwrites the default Django ``__repr__()`` method which would return ``<Bed: Bed object (id)>``.
        It is used for logging.

        :return: The canonical string representation of the bed
        :rtype: str
        """
        return f"<Bed (number: {self.id})>"

    class Meta:
        verbose_name = _("bed")
        verbose_name_plural = _("beds")
