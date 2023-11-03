"""
URLconf for login-protected views of the cms package.
"""
from django.urls import include, path

from ..views import authentication, index, intake_form_view
from ..views.utility.autocomplete import autocomplete_icd10, autocomplete_patient

urlpatterns = [
    path("", index.IndexView.as_view(), name="index"),
    path("intake/", intake_form_view.IntakeFormView.as_view(), name="intake"),
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
]
