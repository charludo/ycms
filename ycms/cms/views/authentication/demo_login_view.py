import logging

from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from ...models import User

logger = logging.getLogger(__name__)


class DemoLoginView(TemplateView):
    """
    View allowing new users sign in without a password - DEMO ONLY
    """

    template_name = "authentication/demo_login.html"

    def get_context_data(self, **kwargs):
        """
        Return the keyword arguments for this view

        :param kwargs: The supplied keyword arguments
        :type kwargs: dict

        :return: a template response
        :rtype: ~django.template.response.TemplateResponse
        """
        return {
            # "users": User.objects.filter(is_active=True, is_staff=False),
            "users": User.objects.filter(is_active=True),
            **super().get_context_data(),
        }

    def post(self, request, *args, **kwargs):
        r"""
        Force-login the given user

        :param request: The current request
        :type request: ~django.http.HttpRequest

        :param \*args: The supplied arguments
        :type \*args: list

        :param \**kwargs: The supplied keyword arguments
        :type \**kwargs: dict

        :return: Redirect to list of wards
        :rtype: ~django.http.HttpResponseRedirect
        """
        user = get_object_or_404(User, pk=request.POST.get("user"))
        login(request, user)
        return redirect("cms:protected:index")
