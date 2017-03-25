from django.conf.urls import url
from . import views


urlpatterns=[url(r'^$',views.home_view,name='home'),
             url(r'^category',views.Job_Category_List,name='Job_Category_list'),
             url(r'^registeration/',views.registration,name='registeration'),
             url(r'^login/$',views.User_login,name='login'),
             url(r'^logout/$',views.User_Logout,name='logout'),

             ]
