from django.conf.urls import url
from django.contrib import admin

from .views import CreateUser, GetUsers

urlpatterns = [
    url(r'^$', GetUsers.as_view(), name='user_list'),
    url(r'^register/$', CreateUser.as_view(), name='register'),
]