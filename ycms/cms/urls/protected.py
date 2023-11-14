"""
URLconf for login-protected views of the cms package.
"""
from django.urls import include, path

from ..views import authentication, index, patients, ward
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
]
