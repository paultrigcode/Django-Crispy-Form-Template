from django.shortcuts import render
from .forms import CrispyPostForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Post
from django.contrib.messages.views import SuccessMessageMixin




# Create your views here.

class CrispyPostFormView(SuccessMessageMixin,CreateView):
    model = Post
    form_class = CrispyPostForm
    success_url = reverse_lazy('success')
    template_name = 'exampmodelform/modelform.html'
    success_message = "was created successfully"



class CrispyPostFormView2(CreateView):
    model = Post
    form_class = CrispyPostForm
    success_url = reverse_lazy('success')
    template_name = 'exampmodelform/modelform2.html'


def frontform(request):
	return render(request,'exampmodelform/bulma.html')