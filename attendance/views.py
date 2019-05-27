from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from attendance.models import Organization, Meeting, AttendanceRecord
import json

# Create your views here.
def index(request):
    context = {}
    template = 'attendance/home.html'
    return render(request, template, context)


@require_http_methods(["POST"])
def mcc_api(request):
    jsons = json.loads(request.POST["data"])
    return HttpResponse(json.dumps(jsons, indent=3))
