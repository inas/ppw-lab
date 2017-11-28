from django.conf.urls import url
from .views import index, profile, \
    add_session_drones, del_session_drones, clear_session_drones, \
    add_session_soundcard, del_session_soundcard, clear_session_soundcard, \
    add_session_optical, del_session_optical, clear_session_optical, \
    cookie_login, cookie_auth_login, cookie_profile, cookie_clear

# /sol
from .custom_auth import auth_login, auth_logout

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^profile/$', profile, name='profile'),

    # custom auth
    url(r'^custom_auth/login/$', auth_login, name='auth_login'),
    url(r'^custom_auth/logout/$', auth_logout, name='auth_logout'),

    #add/delete drones
    url(r'^add_session_drones/(?P<id>\d+)/$', add_session_drones, name='add_session_drones'),
    url(r'^del_session_drones/(?P<id>\d+)/$', del_session_drones, name='del_session_drones'),
    url(r'^clear_session_drones/$', clear_session_drones, name='clear_session_drones'),

    #add/delete soundcard
    url(r'^add_session_soundcard/(?P<id>\d+)/$', add_session_soundcard, name='add_session_soundcard'),
    url(r'^del_session_soundcard/(?P<id>\d+)/$', del_session_soundcard, name='del_session_soundcard'),
    url(r'^clear_session_soundcard/$', clear_session_soundcard, name='clear_session_soundcard'),

    #add/delete optical
    url(r'^add_session_optical/(?P<id>\d+)/$', add_session_optical, name='add_session_optical'),
    url(r'^del_session_optical/(?P<id>\d+)/$', del_session_optical, name='del_session_optical'),
    url(r'^clear_session_optical/$', clear_session_optical, name='clear_session_optical'),

    # cookie
    url(r'^cookie/login/$', cookie_login, name='cookie_login'),
    url(r'^cookie/auth_login/$', cookie_auth_login, name='cookie_auth_login'),
    url(r'^cookie/profile/$', cookie_profile, name='cookie_profile'),
    url(r'^cookie/clear/$', cookie_clear, name='cookie_clear'), #sekaligus logout dari cookie

]
