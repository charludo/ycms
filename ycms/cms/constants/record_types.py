"""
This module contains all string representations of all valid medical record types
"""
from django.utils.translation import gettext_lazy as _

ADMISSION = "admission"
NOTE = "note"

CHOICES = ((ADMISSION, _("admission")), (NOTE, _("note")))
