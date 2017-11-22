from django.conf.urls import url
from .views import index, profile

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^profile/$', profile, name='profile'),
]
