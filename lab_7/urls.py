from django.conf.urls import url
from .views import index, add_friend, validate_npm, friend_list, delete_friend

urlpatterns = [
     url(r'^$', index, name='index'),
     url(r'^add-friend/$', add_friend, name='add-friend'),
     url(r'^validate-npm/$', validate_npm, name='validate-npm'),
     url(r'^delete-friend/(?P<friend_id>[0-9]+)/$', delete_friend, name='delete-friend'),
     url(r'^get-friend-list/$', friend_list, name='get-friend-list'),
     # url(r'^get-friend-list/$', friend_list_json, name='get-friend-list')
]
