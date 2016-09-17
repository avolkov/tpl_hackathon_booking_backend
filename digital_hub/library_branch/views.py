from django.shortcuts import render

from django.http import JsonResponse

from django.db import models

from library_branch.models import Branch, Calendar
# Create your views here.


def branch_to_json(branch):
    return {
        'id': branch.id,
        'name': branch.name,
        'services': [x.id for x in branch.calendar_set.all().order_by('id')]
    }


def index():
    return "hello, world!"


def branches(request):
    return JsonResponse({
        "branches": [
            branch_to_json(branch) for branch in Branch.objects.all()]})


def tools(request):
    return JsonResponse({"data": "Present"})
