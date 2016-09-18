from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import models

import json
from library_branch.models import Branch, Calendar, Event
# Create your views here.


def branch_to_json(branch):
    return {
        'id': branch.id,
        'name': branch.name,
        'services': [x.id for x in branch.calendar_set.all().order_by('id')]
    }

def calendar_to_json(calendar):
    requirements = []
    if calendar.required_good_standing:
        requirements.append('GOOD_STANDING')
    if calendar.required_3d_cert:
        requirements.append('3D_PRINTER')
    return {
        'id': calendar.id,
        'branchID': calendar.branch.id,
        'type': calendar.name,
        'requirements': requirements,
    }


def index():
    return "hello, world!"


def branches(request):
    return JsonResponse({
        "branches": [
            branch_to_json(branch) for branch in Branch.objects.all()]})


def tools(request):
    return JsonResponse({
        "tools": [
            calendar_to_json(calendar) for calendar in Calendar.objects.all()
        ]})


@csrf_exempt
def booking(request):
    post = request.body
    post = post.decode('utf-8')
    data = json.loads(post)
    calendar = Calendar.objects.filter(id=data['resourceId'])
    #event = Event
    return JsonResponse({'booking': 'works'})
