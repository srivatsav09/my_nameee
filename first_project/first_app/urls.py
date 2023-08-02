from django.urls import path
from first_app import views

#template tagging
app_name = 'first_app'


urlpatterns = [
    #path('',views.index,name='index'),
    #path('admin/',views.index,name='index'),
    #path('help/',views.help,name = 'help'), 
    #path('',views.users,name='users'),
    path('rel/',views.relative,name='relative'),
    path('other/',views.other,name='other')
]