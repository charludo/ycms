import logging

from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from ...forms import BedAssignmentForm
from ...models import BedAssignment

logger = logging.getLogger(__name__)


class BedAssignmentView(TemplateView):
    """
    View to manage bed assignments
    """

    template_name = "bed_assignment/bed_assignment.html"

    def get(self, request, *args, **kwargs):
        """
        This function returns a list of all bed assignments,

        :param request: The current request
        :type request: ~django.http.HttpRequest

        :param args: The supplied arguments
        :type args: list

        :param kwargs: The supplied keyword arguments
        :type kwargs: dict

        :return: Response for filtered offers
        :rtype: ~django.template.response.TemplateResponse
        """
        return render(
            request,
            self.template_name,
            {
                "form": BedAssignmentForm(),
                "bed_assignments": BedAssignment.objects.all(),
                **self.get_context_data(**kwargs),
            },
        )
