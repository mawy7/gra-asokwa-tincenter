from entry.models import Entry, Organization, Dispatch
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('created_date', 'organization', 'number', 'recieved_from', 'contact_number', 'recieving_officer', 'time_of_completion')

    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_class = 'form-horizontal'


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = [
            "name",
            "city"
        ]



class DispatchForm(forms.ModelForm):

    class Meta:
        model = Dispatch
        fields = ('dispatch_date', 'organization', 'dispatched_to', 'dispatching_officer', 'number_rejected', 'number_accepted', 'status', 'complete')

    def __init__(self, *args, **kwargs):
        super(DispatchForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_class = 'form-horizontal'



class RenewBookForm(forms.Form):
    time_of_completion = forms.DateField(help_text="Enter a date between now and 4 weeks (default 1).")

    def time_of_completion(self):
        data = self.cleaned_data['time_of_completion']
        
        # Check if a date is not in the past. 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - time of completion in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - time of completion more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data
