from django.conf.urls import url, include
from django.contrib import admin
from goods import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

]
