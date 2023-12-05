import pytest
from django.test.client import Client
from django.urls import reverse

from ycms.cms.models import User


@pytest.mark.django_db
def test_ward_information_accurate(load_test_data):
    """
    Test if the ward information displayed in the ward view is accurate

    :param load_test_data: The fixture providing the test data (see :meth:`~tests.conftest.load_test_data`)
    :type load_test_data: tuple
    """
    client = Client()
    client.force_login(User.objects.get(pk=1))
    view_name = "cms:protected:ward_detail"
    endpoint = reverse(view_name, kwargs={"pk": 1})
    response = client.get(endpoint, {}, format="html", content_type="text/html")
    assert response.status_code == 200
    assert response.context["patient_info"]["total_patients"]() == 10
    assert response.context["patient_info"]["female_patients"]() == 5
    assert response.context["patient_info"]["male_patients"]() == 5
    assert response.context["ward"].available_beds == 18
    assert response.context["ward"].total_beds == 28


@pytest.mark.django_db
def test_discharge_working(load_test_data):
    """
    Test if the ward information displayed is correct after discharging a patient

    :param load_test_data: The fixture providing the test data (see :meth:`~tests.conftest.load_test_data`)
    :type load_test_data: tuple
    """
    client = Client()
    client.force_login(User.objects.get(pk=1))

    view_name = "cms:protected:discharge_patient"
    endpoint = reverse(view_name, kwargs={"assignment_id": 19})
    response = client.post(endpoint, {}, content_type="application/json")
    assert response.status_code == 200

    view_name = "cms:protected:ward_detail"
    endpoint = reverse(view_name, kwargs={"pk": 1})
    response = client.get(endpoint, {}, format="html", content_type="text/html")
    assert response.status_code == 200
    assert response.context["patient_info"]["total_patients"]() == 9
    assert response.context["patient_info"]["female_patients"]() == 4
    assert response.context["patient_info"]["male_patients"]() == 5
    assert response.context["ward"].available_beds == 19
    assert response.context["ward"].total_beds == 28
