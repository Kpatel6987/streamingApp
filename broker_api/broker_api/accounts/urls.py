from django.conf.urls import url
from django.contrib import admin

from .views import ListCreateAccount, RetrieveAccount

urlpatterns = [
    url(r'^$', ListCreateAccount.as_view(), name='accounts'),
    url(r'^(?P<pk>[0-9]+)$', RetrieveAccount.as_view(), name='account'),
]