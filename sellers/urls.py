from django.conf.urls import url, include
from django.contrib import admin
from sellers import views

urlpatterns = [
    url(r'^sellers/$', views.sellers, name='sellers'),

]
