from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,User
from . import forms
# Create your views here.


def index(request):
    #webpages_list = AccessRecord.objects.order_by('date')
    #date_dict = {'access_records':webpages_list}
    #my_dict = {'insert_me' : "Hello i am from views.py!"}
    #return render(request,'first_app/index.html',context=date_dict)
    return render(request,'first_app/index.html')
    # return render(request,'first_app/index.html')

def help(request):
    my_dict1 = {'help' : "this is the help page"}
    return render(request,'first_app/help.html',context=my_dict1)

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'first_app/users.html',context=user_dict)
