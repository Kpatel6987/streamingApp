from django.conf.urls import url
from django.contrib import admin

from .views import GetAccounts

urlpatterns = [
    url(r'^$', GetAccounts.as_view(), name='account_list'),
    # url(r'^register/$', CreateUser.as_view(), name='register'),
]