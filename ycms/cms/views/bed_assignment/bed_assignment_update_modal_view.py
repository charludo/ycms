from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import UpdateView

from ...forms import BedAssignmentForm
from ...models import BedAssignment


class BedAssignmentUpdateModalView(UpdateView):
    """
    View to update a patient in a modal
    """

    model = BedAssignment
    template_name = "bed_assignment/update_bed_assignment_modal.html"
    form_class = BedAssignmentForm

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests if needed
        """
        assignment_id = kwargs.get("pk")
        assignment = get_object_or_404(BedAssignment, pk=assignment_id)
        form = BedAssignmentForm(instance=assignment, is_update=True)
        return render(request, self.template_name, {"form": form})
