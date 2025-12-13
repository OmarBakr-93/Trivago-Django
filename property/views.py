from django.shortcuts import render, redirect
from django.views.generic import  DetailView, CreateView
from .models import Property
from django.views.generic.edit import FormMixin
from .forms import PropertyBookingForm
from .filters import PropertyFilter
from django_filters.views import FilterView


# Create your views here.

class PropertyList(FilterView):
  model = Property
  filterset_class = PropertyFilter
  template_name = 'property/property_list.html'
  paginate_by = 1
  
  
  
class PropertyDetail(FormMixin, DetailView):
  model = Property
  form_class = PropertyBookingForm
  
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['related'] = Property.objects.filter(category=self.get_object().category)[:3]
    return context
  
  def post(self, request, *args, **kwargs):
    form = self.get_form()
    if form.is_valid():
      my_form = form.save(commit=False)
      my_form.property = self.get_object()
      my_form.user = request.user
      my_form.save()
      return redirect('/', status=302)
    else:
      return self.form_invalid(form)
  # book
  
  
class AddListing(CreateView):
  pass