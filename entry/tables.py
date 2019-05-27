import django_tables2 as tables
from .models import Entry, Dispatch

class EntryTable(tables.Table):
    class Meta:
        model = Entry
        template_name = 'django_tables2/bootstrap-responsive.html'


class DispatchTable(tables.Table):
    class Meta:
        model = Dispatch
        template_name = 'django_tables2/bootstrap-responsive.html'