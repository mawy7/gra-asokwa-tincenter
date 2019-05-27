from rest_framework import routers
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from entry import views
from entry.views import EntryViewsSets, OrganizationCreatePopup, OrganizationEditPopup, get_organization_id, entries

app_name = 'entry'
router = routers.DefaultRouter()
router.register(r'entry', EntryViewsSets)

urlpatterns = [
    path('ent', view=views.entry, name='entry'),
    path('entries', view=views.entries, name='entries'),
     path('dispatched', view=views.dispatched, name='dispatched'),
    path('submit_entry', login_required(views.submit_entry), name='submit_entry'),
    path('new_dispatch', login_required(views.submit_dispatch), name='submit_dispatch'),
    path('submitted', login_required(views.SuccessView.as_view()), name='submitted'),
    path('dispatch', login_required(views.SuccessDispatchView.as_view()), name='dispatched'),
    
]