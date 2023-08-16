from django.urls import path,re_path,include
from cbv_app import views

app_name = 'cbv_app'
urlpatterns =[
    path('',views.SchoolListView.as_view(),name='list'),
    re_path(r'^(?P<pk>[-\w]+)/$',views.SchoolDetailView.as_view(),name='detail'),
]