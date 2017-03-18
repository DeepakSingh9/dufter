from django.conf.urls import url
from . import views

urlpatterns=[url('',views.Post_List,name='Post_List')
             ,]