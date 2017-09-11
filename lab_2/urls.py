from django.conf.urls import url
from .views import index

#url for app, add your URL Configuration

urlpatterns = [
#TODO Implement this
	url(r'^lab_2/', index, name='index_lab2'),
]
