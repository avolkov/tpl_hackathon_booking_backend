from django import forms
from library_branch.models import Event


class EventAdminForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = Event
        widgets = {}
