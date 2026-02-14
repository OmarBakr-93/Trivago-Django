from django import forms
from .models import Property_book


class PropertyBookingForm(forms.ModelForm):
  date_from = forms.DateField(widget=forms.DateInput(attrs={'id': 'checkin_date'}))
  date_to = forms.DateField(widget=forms.DateInput(attrs={'id': 'checkout_date'}))
  class Meta:
    model = Property_book
    fields = ['date_from', 'date_to', 'guest', 'children']

