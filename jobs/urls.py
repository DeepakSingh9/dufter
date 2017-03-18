from django.conf.urls import url
from . import views

urlpatterns=[
             url(r'category/',views.Job_Category_List,name='Job_Category_list'),
             url(r'login/',views.user_login,name='user_login'),
             ]