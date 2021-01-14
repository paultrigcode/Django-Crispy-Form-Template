from django.shortcuts import render

# Create your views here.

from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

# from .forms import AddressForm
from .forms import AddressForm, CrispyAddressForm, CustomFieldForm



class AddressFormView(FormView):
    form_class = AddressForm
    success_url = reverse_lazy('success')


class CrispyAddressFormView(FormView):
    form_class = CrispyAddressForm
    success_url = reverse_lazy('success')
    template_name = 'exampform/crispy_form.html'


class CustomFieldFormView(FormView):
    form_class = CustomFieldForm
    success_url = reverse_lazy('success')
    template_name = 'exampform/crispy_form.html'


class SuccessView(TemplateView):
    template_name = 'exampform/success.html'
