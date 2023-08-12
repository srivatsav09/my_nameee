from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse

#from first_app.models import Topic,Webpage,AccessRecord,User

from django.contrib.auth import authenticate,login,logout
from first_app.forms import UserForm,UserProfileImfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from . import forms
#from first_app.forms import NewUserForm
# Create your views here.


def index(request):
    return render(request,'first_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def registration(request):
    registered = False
    if request.method =="POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileImfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'prof_pic' in request.FILES:
                profile.prof_pic = request.FILES['prof_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileImfoForm()
    
    return render(request,'first_app/registration.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password = password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("someone tried to login and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details provided!!")
    else:
        return render(request,'first_app/login.html',{})

# def index(request):
#     #webpages_list = AccessRecord.objects.order_by('date')
#     #date_dict = {'access_records':webpages_list}
#     #my_dict = {'insert_me' : "Hello i am from views.py!"}
#     #return render(request,'first_app/index.html',context=date_dict)
#     context_dict = {'text':'hello world','number':100}
#     return render(request,'first_app/index.html',context_dict)
#     # return render(request,'first_app/index.html')

# def other(request):
#     return render(request,'first_app/other.html')

# def relative(request):
#     return render(request,'first_app/rel_templates.html')

# def users(request):

#     form = NewUserForm()

#     if request.method == "POST":
#         form = NewUserForm(request.POST)

#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#         else:
#             print("error form invalid")
#     return render(request,"first_app/users.html",{"form":form})

# def form_name_view(request):
#     form = forms.FormName()

#     if request.method=="POST":
#         form=forms.FormName(request.POST)

#         if form.is_valid():
#             #DO SOMETHING
#                 print("VALIDATION SUCCESS!")
#                 print("NAME: " + form.cleaned_data['name'])
#                 print("EMAIL: " + form.cleaned_data['email'])
#                 print("TEXT: " + form.cleaned_data['text'])

#     return render(request,'first_app/form_page.html',{'form':form})

# def help(request):
#     my_dict1 = {'help' : "this is the help page"}
#     return render(request,'first_app/help.html',context=my_dict1)

# def users(request):
#     user_list = User.objects.order_by('first_name')
#     user_dict = {'users':user_list}
#     return render(request,'first_app/users.html',context=user_dict)
