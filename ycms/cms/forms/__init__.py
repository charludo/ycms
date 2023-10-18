"""
Forms for creating and modifying database objects.
Please refer to :mod:`django.forms` for general information about Django forms (see also: :doc:`django:topics/forms/index`).
"""
from .authentication.password_reset_request_form import PasswordResetRequestForm
from .authentication.registration_form import RegistrationForm
from .patients.patient_form import PatientForm
