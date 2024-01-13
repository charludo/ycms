"""
URLconf for login-protected views of the cms package.
"""
from django.urls import include, path

from ..views import authentication, bed_assignment, index, patients, timeline, ward
from ..views.utility.autocomplete import autocomplete_icd10, autocomplete_patient

urlpatterns = [
    path("", index.UserBasedRedirectView.as_view(), name="index"),
    path(
        "patients/",
        include(
            [
                path("", patients.PatientsListView.as_view(), name="patients"),
                path(
                    "create/",
                    patients.PatientCreateView.as_view(),
                    name="create_patient",
                ),
                path(
                    "update/<int:patient>/<int:bed_assignment>/",
                    patients.UpdatePatientStayView.as_view(),
                    name="update_patient_stay",
                ),
                path(
                    "update/<int:pk>/",
                    patients.PatientUpdateView.as_view(),
                    name="update_patient",
                ),
                path(
                    "delete/<int:pk>",
                    patients.PatientDeleteView.as_view(),
                    name="delete_patient",
                ),
                path(
                    "discharge/<int:assignment_id>/",
                    patients.DischargePatientView.as_view(),
                    name="discharge_patient",
                ),
                path(
                    "assign/<int:ward_id>/<int:assignment_id>/",
                    patients.AssignPatientView.as_view(),
                    name="assign_patient",
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
    path(
        "ward/",
        include(
            [
                path("", ward.WardView.as_view(), name="ward_detail_default"),
                path("<int:pk>/", ward.WardView.as_view(), name="ward_detail"),
                path(
                    "manage/", ward.WardManagementView.as_view(), name="ward_management"
                ),
            ]
        ),
    ),
    path(
        "timeline/",
        include(
            [
                path("<int:pk>/", timeline.TimelineView.as_view(), name="timeline"),
                path(
                    "mode-switch/<int:pk>/",
                    timeline.ModeSwitchView.as_view(),
                    name="mode_switch",
                ),
            ]
        ),
    ),
    path(
        "bed-assignments/",
        include(
            [
                path(
                    "",
                    bed_assignment.BedAssignmentView.as_view(),
                    name="manage_bed_assignment",
                )
            ]
        ),
    ),
]
