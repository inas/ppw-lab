from django.conf.urls import url
from .views import index
import lab_3.urls as lab_3

#url for app
urlpatterns = [
        url(r'^$', index, name='index'),
        url(r'^lab-3/', include(lab_3,namespace='lab-3')),
]
