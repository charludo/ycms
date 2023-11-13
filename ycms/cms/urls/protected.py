"""
URLconf for login-protected views of the cms package.
"""
from django.urls import include, path

from ..views import authentication, bed_assignment, index, patients, ward
from ..views.utility.autocomplete import autocomplete_icd10, autocomplete_patient

urlpatterns = [
    path("", index.UserBasedRedirectView.as_view(), name="index"),
    path(
        "patients/",
        include(
            [
                path("", patients.PatientsListView.as_view(), name="patients"),
                path(
                    "discharge/<int:assignment_id>/",
                    patients.DischargePatientView.as_view(),
                    name="discharge_patient",
                ),
            ]
        ),
    ),
    path("intake/", patients.IntakeFormView.as_view(), name="intake"),
    path(
        "accounts/",
        include(
            [
                path(
                    "create-user/",
                    authentication.RegistrationView.as_view(),
                    name="create_user",
                )
            ]
        ),
    ),
    path(
        "autocomplete/",
        include(
            [
                path("icd10/", autocomplete_icd10, name="autocomplete_icd10"),
                path("patient/", autocomplete_patient, name="autocomplete_patient"),
            ]
        ),
    ),
    path("ward/", ward.WardView.as_view(), name="ward_detail_default"),
    path("ward/<int:pk>/", ward.WardView.as_view(), name="ward_detail"),
    path(
        "discharge-patient/<int:assignment_id>/",
        patients.DischargePatientView.as_view(),
        name="discharge_patient",
    ),
    path(
        "bed-assignments/",
        include(
            [
                path(
                    "",
                    bed_assignment.BedAssignmentView.as_view(),
                    name="manage_bed_assignment",
                ),
                path(
                    "create/",
                    bed_assignment.BedAssignmentCreateView.as_view(),
                    name="create_bed_assignment",
                ),
                path(
                    "update/<int:pk>/",
                    bed_assignment.BedAssignmentUpdateView.as_view(),
                    name="update_bed_assignment",
                ),
            ]
        ),
    ),
]
