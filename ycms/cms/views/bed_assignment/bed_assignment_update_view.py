import logging

from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.edit import UpdateView

from ...forms import BedAssignmentForm
from ...models import BedAssignment

logger = logging.getLogger(__name__)


class BedAssignmentUpdateView(UpdateView):
    """
    View allowing to update the bed assignment
    """

    model = BedAssignment
    template_name = "bed_assignment/update_bed_assignment.html"
    form_class = BedAssignmentForm
    success_url = reverse_lazy("cms:protected:manage_bed_assignment")

    def get_form_kwargs(self):
        """
        Return the keyword arguments for instantiating the form

        :return: The form kwargs
        :rtype: dict
        """
        kwargs = super().get_form_kwargs()
        kwargs["is_update"] = True
        return kwargs
