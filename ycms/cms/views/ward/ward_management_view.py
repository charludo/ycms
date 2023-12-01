from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from ...constants import job_types
from ...decorators import permission_required
from ...forms import WardForm
from ...models import User, Ward


@method_decorator(permission_required("cms.change_ward"), name="dispatch")
class WardManagementView(TemplateView):
    """
    View to see all wards data and add a new one
    """

    template_name = "ward/ward_management.html"

    def get(self, request, *args, **kwargs):
        r"""
        This function returns a list of all wards,
        as well as a form for creating a new one

        :param request: The current request
        :type request: ~django.http.HttpRequest

        :param \*args: The supplied arguments
        :type \*args: list

        :param \**kwargs: The supplied keyword arguments
        :type \**kwargs: dict


        :return: List of all wards
        :rtype: ~django.template.response.TemplateResponse
        """
        ward_form = WardForm()

        return render(
            request,
            self.template_name,
            {
                "ward_form": ward_form,
                **self._get_ward_info(),
                **super().get_context_data(**kwargs),
            },
        )

    @staticmethod
    def _get_ward_info():
        wards = Ward.objects.all()
        return {
            "wards": wards,
            "wards_count": wards.count(),
            "beds_count": sum(ward.total_beds for ward in wards),
            "occupied_beds": sum(ward.occupied_beds for ward in wards),
            "available_beds": sum(ward.available_beds for ward in wards),
            "doctors_count": User.objects.filter(job_type=job_types.DOCTOR).count(),
            "nurses_count": User.objects.filter(job_type=job_types.NURSE).count(),
        }

    def post(self, request, *args, **kwargs):
        r"""

        :param request: The current request
        :type request: ~django.http.HttpRequest

        :param \*args: The supplied arguments
        :type \*args: list

        :param \**kwargs: The supplied keyword arguments
        :type \**kwargs: dict

        :return: Redirect to list of wards
        :rtype: ~django.http.HttpResponseRedirect
        """
        ward_form = WardForm(
            data=request.POST, additional_instance_attributes={"creator": request.user}
        )
        if not ward_form.is_valid():
            ward_form.add_error_messages(request)
            return render(
                request,
                self.template_name,
                {
                    "ward_form": ward_form,
                    **self._get_ward_info(),
                    **super().get_context_data(**kwargs),
                },
            )
        ward = ward_form.save()
        messages.success(
            request, _('Addition of new ward "{}" successful!').format(ward.name)
        )
        return redirect("cms:protected:ward_management")
