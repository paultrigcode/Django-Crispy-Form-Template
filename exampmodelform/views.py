from django.shortcuts import render
from .forms import CrispyPostForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Post



# Create your views here.

class CrispyPostFormView(CreateView):
    model = Post
    form_class = CrispyPostForm
    success_url = reverse_lazy('success')
    template_name = 'exampmodelform/modelform.html'
