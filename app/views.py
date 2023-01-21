from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from app.forms import * 

# Create your views here.
class cbv_forms(FormView):
    template_name='cbv_forms.html'
    form_class=NameForm

    def form_valid(self, form): 
        return  HttpResponse(str(form.cleaned_data))


class cbv_modelforms(FormView):
    template_name='cbv_modelforms.html'
    form_class=StudentForm

    def form_valid(self, form): 
        form.save()
        return  HttpResponse('inserted successfully...')