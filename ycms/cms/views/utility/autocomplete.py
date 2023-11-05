"""
Utility views for autocompleting various user inputs
"""
from django.db.models import Q
from django.http import JsonResponse

from ...models import ICD10Entry, Patient


def autocomplete_icd10(request):
    """
    Function to autocomplete search queries for ICD-10-GM codes or descriptions

    :param request: The current request submitting the form
    :type request: ~django.http.HttpRequest

    :return: JSON object containing search results
    :rtype: str
    """
    query = request.GET.get("q", "")
    results = ICD10Entry.objects.filter(
        Q(code__icontains=query) | Q(description__icontains=query)
    )[:15]
    return JsonResponse(
        {
            "suggestions": [
                {"id": result.id, "name": f"{result.code} --- {result.description}"}
                for result in results
            ]
        }
    )


def autocomplete_patient(request):
    """
    Function to autocomplete search queries for patients

    :param request: The current request submitting the form
    :type request: ~django.http.HttpRequest

    :return: JSON object containing search results
    :rtype: str
    """
    query = request.GET.get("q", "")
    results = Patient.objects.filter(
        Q(last_name__icontains=query)
        | Q(first_name__icontains=query)
        | Q(date_of_birth__icontains=query)
    )[:15]
    return JsonResponse(
        {
            "suggestions": [
                {
                    "id": result.id,
                    "name": f"{result.last_name}, {result.first_name}, {result.date_of_birth}",
                }
                for result in results
            ]
        }
    )
