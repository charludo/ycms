"""
This module contains the possible names of roles to make them translatable.
"""
from django.utils.translation import gettext_lazy as _

MANAGER = "MANAGER"
DOCTOR = "DOCTOR"
NURSE = "NURSE"

#: Choices for staff roles
CHOICES = [(MANAGER, _("Manager")), (DOCTOR, _("Doctor")), (NURSE, _("Nurse"))]
