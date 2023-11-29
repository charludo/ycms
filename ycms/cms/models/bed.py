from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from ..constants import bed_types
from .abstract_base_model import AbstractBaseModel
from .room import Room
from .timetravel_manager import current_or_travelled_time
from .user import User


class Bed(AbstractBaseModel):
    """
    Data model representing a Bed.
    """

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=current_or_travelled_time, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    bed_type = models.CharField(
        max_length=10,
        choices=bed_types.CHOICES,
        verbose_name=_("bed type"),
        help_text=_("specialty bed types may be available"),
    )
    room = models.ForeignKey(
        Room,
        related_name="beds",
        on_delete=models.CASCADE,
        verbose_name=_("room"),
        help_text=_("The room this bed belongs to"),
    )

    @cached_property
    def is_available(self):
        """
        Helper property to check if the bed is available. Returns True if there
        is no bed assignment to this bed with a discharge date in the future.

        :return: if the bed is available
        :rtype: bool
        """                
        if self.assignments.exists():            
            active_assignments = self.assignments.filter(
                models.Q(admission_date__lte=current_or_travelled_time())
                & (
                    models.Q(discharge_date__gt=current_or_travelled_time())
                    | models.Q(discharge_date__isnull=True)
                )
            )
            return not active_assignments.exists()        
        return True

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
