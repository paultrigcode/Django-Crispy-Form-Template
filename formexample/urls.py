"""formexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from exampform import views
from exampmodelform import views as piews
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='/form/1/'), name='index'),
    path('admin/', admin.site.urls),
    path('form/1/', views.AddressFormView.as_view(template_name='exampform/form_1.html'), name='form_1'),
    path('form/2/', views.AddressFormView.as_view(template_name='exampform/form_2.html'), name='form_2'),
    path('form/3/', views.AddressFormView.as_view(template_name='exampform/form_3.html'), name='form_3'),
    path('form/4/', views.CrispyAddressFormView.as_view(), name='form_4'),
    path('form/5/', views.CustomFieldFormView.as_view(),name ='form_5'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('form/6/', piews.CrispyPostFormView.as_view(), name='form_6'),
    path('form/7/', piews.CrispyPostFormView2.as_view(), name='form_7'),
    path('form/8/', piews.frontform,name='form_8'),




]
