"""
Forms for creating and modifying database objects.
Please refer to :mod:`django.forms` for general information about Django forms (see also: :doc:`django:topics/forms/index`).
"""
from .authentication.password_reset_request_form import PasswordResetRequestForm
from .authentication.registration_form import RegistrationForm
from .intake_bed_assignment_form import IntakeBedAssignmentForm
from .intake_record_form import IntakeRecordForm
from .patient_form import PatientForm
