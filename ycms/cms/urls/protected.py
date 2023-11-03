"""
URLconf for login-protected views of the cms package.
"""
from django.urls import include, path

from ..views import authentication, index

urlpatterns = [
    path("", index.IndexView.as_view(), name="index"),
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
]
