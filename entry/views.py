from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, UpdateView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, render_to_response
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from datetime import datetime
from rest_framework import viewsets
from django.template import RequestContext
from django.shortcuts import render
from .models import Entry, Dispatch
from .forms import EntryForm, OrganizationForm, DispatchForm
from .serializers import EntrySerializer
from django.views.decorators.csrf import csrf_exempt
import json

from .tables import EntryTable, DispatchTable
import django_tables2 as tables
from django_tables2 import RequestConfig
from django_tables2.export.views import ExportMixin
#from timeline_logger.models import TimelineLog
# Create your views here.

@login_required(login_url='/accounts/login/')
def entry(request):
    context = {}
    template = 'entry.html'
    return render(request, template, context)
    
@login_required(login_url='/accounts/login/')
def entries(request):
    table = EntryTable(Entry.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)
    return render(request, 'entries.html', {'table': table})

class TableView(ExportMixin, tables.SingleTableView):
    table_class = EntryTable
    model = Entry
    template_name = 'django_tables2/bootstrap-responsive.html'


@login_required(login_url='/accounts/login/')
def dispatched(request):
    table_dispatch = DispatchTable(Dispatch.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table_dispatch)
    return render(request, 'dispatched_table.html', {'table_dispatch': table_dispatch})


class TableViewDis(ExportMixin, tables.SingleTableView):
    table_class = DispatchTable
    model = Dispatch
    template_name = 'django_tables2/bootstrap-responsive.html'


@login_required
def submit_entry(request):
	assert isinstance(request, HttpRequest)

	if request.method == "POST":
		entry_form = EntryForm(request.POST)

		if entry_form.is_valid():
            # process the data in form.cleaned_data as required
			obj = Entry()  # gets new object
			obj.user_id = request.user.pk
			obj.created_date = entry_form.cleaned_data['created_date']
			obj.organization = entry_form.cleaned_data['organization']
			obj.number = entry_form.cleaned_data['number']
			obj.recieved_from = entry_form.cleaned_data['recieved_from']
			obj.contact_number = entry_form.cleaned_data['contact_number']
			obj.recieving_officer = entry_form.cleaned_data['recieving_officer']
			obj.time_of_completion = entry_form.cleaned_data['time_of_completion']
			#obj.user = entry_form.cleaned_data['user']
			# finally save the object in db
			obj.save()
			
			return HttpResponseRedirect(reverse('entry:submitted'))

	else:
		form = EntryForm()

		return render(
			request,
			"newentry.html",
			{
				'created_date': 'Submit an Entry',
				'year': datetime.now().year,
				'form': form,
			}
		)


class EntryView(UpdateView):
    template_name = "entries.html"
    form_class = EntryForm
    model = Entry
    success_url = reverse_lazy('entry:submitted')

    def get_context_data(self, **kwargs):
        context = super(EntryView, self).get_context_data(**kwargs)
        context['organization'] = "Entry Details"
        context['year'] = datetime.now().year
        context['number'] = get_object_or_404(Entry, pk=self.kwargs['pk'])
        context['entrys'] = Entry.objects.filter(user=self.request.user.pk)
        return context




class EntryViewsSets(viewsets.ReadOnlyModelViewSet):
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()



class SuccessView(TemplateView):
    template_name = "success.html"

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        context['title'] = 'Entry Submission Successful'
        context['year'] = datetime.now().year
        return context



def OrganizationCreatePopup(request):
	form = OrganizationForm(request.POST or None)
	if form.is_valid():
		instance = form.save()

		## Change the value of the "#id_organization". This is the element id in the form
		
		return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_organization");</script>' % (instance.pk, instance))
	
	return render(request, "organization_form.html", {"form" : form})

def OrganizationEditPopup(request, pk = None):
	instance = get_object_or_404(Organization, pk = pk)
	form = OrganizationForm(request.POST or None, instance = instance)
	if form.is_valid():
		instance = form.save()
		
		## Change the value of the "#id_organization". This is the element id in the form
		
		return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_organization");</script>' % (instance.pk, instance))

	return render(request, "organization_form.html", {"form" : form})

@csrf_exempt
def get_organization_id(request):
	if request.is_ajax():
		organization_name = request.GET['organization_name']
		organization_city = request.GET['organization_city']
		organization_id = Organization.objects.get(name = organization_name).id
		data = {'organization_id':organization_id,}
		return HttpResponse(json.dumps(data), content_type='application/json')
	return HttpResponse("/")




@login_required
def submit_dispatch(request):
	assert isinstance(request, HttpRequest)

	if request.method == "POST":
		entry_form = DispatchForm(request.POST)

		if entry_form.is_valid():
            # process the data in form.cleaned_data as required
			obj = Dispatch()  # gets new object
			obj.user_id = request.user.pk
			obj.dispatch_date = entry_form.cleaned_data['dispatch_date']
			obj.organization = entry_form.cleaned_data['organization']
			obj.complete = entry_form.cleaned_data['complete']
			obj.dispatching_officer = entry_form.cleaned_data['dispatching_officer']
			obj.number_rejected = entry_form.cleaned_data['number_rejected']
			obj.number_accepted = entry_form.cleaned_data['number_accepted']
			obj.status = entry_form.cleaned_data['status']
			obj.dispatched_to = entry_form.cleaned_data['dispatched_to']
			#obj.user = entry_form.cleaned_data['user']
			# finally save the object in db
			obj.save()
			
			return HttpResponseRedirect(reverse('entry:dispatched'))

	else:
		form = DispatchForm()

		return render(
			request,
			"dispatch.html",
			{
				'dispatch_date': 'Submit an Dispatch',
				'year': datetime.now().year,
				'form': form,
			}
		)




class SuccessDispatchView(TemplateView):
    template_name = "dispatched.html"

    def get_context_data(self, **kwargs):
        context = super(SuccessDispatchView, self).get_context_data(**kwargs)
        context['title'] = 'Dispatch Successful'
        context['year'] = datetime.now().year
        return context
