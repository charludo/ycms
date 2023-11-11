from django.shortcuts import redirect
from django.views.generic.detail import DetailView

from ...constants import gender
from ...models import Ward


class WardView(DetailView):
    """
    View to see a ward
    """

    model = Ward
    template_name = "ward/ward.html"
    context_object_name = "ward"

    def get_context_data(self, **kwargs):
        """
        This function returns a list of all rooms in the ward

        :param kwargs: The supplied keyword arguments
        :type kwargs: dict

        :return: Response for filtered offers
        :rtype: ~django.template.response.TemplateResponse
        """
        ward_id = self.kwargs.get("pk")
        ward = Ward.objects.get(id=ward_id)
        rooms = ward.rooms.all()
        wards = Ward.objects.all()
        return {
            "rooms": rooms,
            "corridor_index": str(len(rooms) // 2),
            "ward": ward,
            "patient_info": self._get_patient_info(ward.patients),
            "wards": wards,
            "selected_ward_id": ward_id,
            **super().get_context_data(**kwargs),
        }

    def _get_patient_info(self, patients):
        patient_info = {}
        patient_info["total_patients"] = patients.count
        patient_info["female_patients"] = patients.filter(gender=gender.FEMALE).count
        patient_info["male_patients"] = patients.filter(gender=gender.MALE).count
        return patient_info

    def post(self, request, *args, **kwargs):
        """
        This function handles the post request for ward view
        """
        if selected_ward_id := request.POST.get("ward"):
            return redirect("cms:protected:ward_detail", pk=selected_ward_id)
        return redirect("cms:protected:index")
