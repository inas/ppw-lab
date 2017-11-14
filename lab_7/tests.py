from django.test import TestCase
from .views import index, friend_list, get_friend_list
from django.test import Client
from django.urls import resolve
# Create your tests here.
class Lab6UnitTest(TestCase):

	def test_lab_7_url_is_exist(self):
		response = Client().get('/lab-7/')
		self.assertEqual(response.status_code, 200)

	def test_lab7_using_index_func(self):
		found = resolve('/lab-7/')
		self.assertEqual(found.func, index)

	def test_friend_list_url_is_exist(self):
		response = Client().get('/lab-7/friend-list/')
		self.assertEqual(response.status_code, 200)

	def test_friend_list_using_index_func(self):
		found = resolve('/lab-7/friend-list/')
		self.assertEqual(found.func, friend_list)

	def test_get_friend_list_data_url_is_exist(self):
		response = Client().get('/lab-7/get-friend-list/')
		self.assertEqual(response.status_code, 200)

	def test_getfriendlist_using_index_func(self):
		found = resolve('/lab-7/get-friend-list/')
		self.assertEqual(found.func, get_friend_list)