from django import forms
from .models import Property_book


class PropertyBookingForm(forms.ModelForm):
  class Meta:
    model = Property_book
    fields = ['date_from', 'date_to', 'guest', 'children']

