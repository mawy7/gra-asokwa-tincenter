from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.conf.urls import handler404, handler500
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from home import views
from entry.views import OrganizationCreatePopup, OrganizationEditPopup, get_organization_id


urlpatterns = [
	path('', include('home.urls', namespace='home')),
    path('accounts/', include('registration.backends.default.urls')),
    #path('accounts/', include('registration.backends.simple.urls')),
    path('profile/', include('registration.urls', namespace='profiles')),
    path('entry/', include('entry.urls', namespace='entry')),
    path('todo/', include('todo.urls', namespace="todo")),
    path('attendance/', include('attendance.urls', namespace="attendance")),
    path('tinadmin/', include('tinadmin.urls', namespace="register")),
    url(r'^organization/create', OrganizationCreatePopup, name = "OrganizationCreate"),
    url(r'^organization/(?P<pk>\d+)/edit', OrganizationEditPopup, name = "OrganizationEdit"),
    url(r'^organization/ajax/get_organization_id', get_organization_id, name = "get_organization_id"),
    url(r'^schedule/', include('schedule.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.

handler404 = 'home.views.handler404'



