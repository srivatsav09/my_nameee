from typing import Any, Dict
from django.shortcuts import render
from . import models
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
# Create your views here.


# def index(request):
#     return render(request,'index.html')


# class CBView(View):
#     def get(self,request):
#         return HttpResponse("CLASS BASED VIEWS HAVE BEEN USED!")

class IndexView(TemplateView):
    template_name = 'index.html'
    
#     def get_context_data(self, **kwargs: Any):
#         context =  super().get_context_data(**kwargs)
#         context['injectme'] = 'basic injection'
#         return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model=models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'cbv_app/school_detail.html'