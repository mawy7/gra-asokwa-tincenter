from django.shortcuts import render, render_to_response
from django.template import RequestContext

from entry.models import Entry, Dispatch, Organization
from todo.models import Task
# Create your views here.



def home(request):
    countE= Entry.objects.all().count()
    countT= Task.objects.all().count()
    countD= Dispatch.objects.all().count()
    countO= Organization.objects.all().count()
    context= {'countE': countE, 'countT': countT, 'countD': countD, 'countO': countO}
    template = 'homepage.html'
    return render(request, template, context)



def summary(request):
    countE= Entry.objects.all().count()
    countT= Task.objects.all().count()
    countD= Dispatch.objects.all().count()
    countO= Organization.objects.all().count()
    context= {'countE': countE, 'countT': countT, 'countD': countD, 'countO': countO}
    template = 'summary.html'
    return render(request, template, context)



def handler404(request, exception):
    return render(request, '404.html', locals())

