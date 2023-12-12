from django.urls import path,re_path,include
from cbv_app import views

app_name = 'cbv_app'
urlpatterns =[
    path('ok',views.SchoolListView.as_view(),name='list'),
    re_path(r'^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name='detail'),
    path('create',views.SchoolCreateView.as_view(),name='create'),
    re_path(r'update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name='update'),
    re_path(r'delete/(?P<pk>\d+)/$',views.SchoolDeleteView.as_view(),name='delete'),
    path('',views.upload,name='upload'),
    path('success',views.success_page,name="success_page"),
]