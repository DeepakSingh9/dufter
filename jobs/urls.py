from django.conf.urls import url
from . import views


urlpatterns=[
             url(r'category/',views.Job_Category_List,name='Job_Category_list'),
             url(r'register/',views.user_registration,name='user_registration'),
             url(r'edit/',views.edit,name='edit'),
             ]