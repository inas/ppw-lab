from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, add_friend, validate_npm, delete_friend, friend_list, get_friend_list, paginate_page
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.manager import Manager
from unittest.mock import patch
from .models import Friend
from .api_csui_helper.csui_helper import CSUIhelper

# Create your tests here.
class Lab7UnitTestCase(TestCase):
	def test_lab_7_url_is_exists(self):
		response = Client().get('/lab-7/')
		self.assertEqual(response.status_code,200)

	def test_lab_7_using_index_func(self):
		found = resolve('/lab-7/')
		self.assertEqual(found.func, index)

	def test_friend_list_url_is_exist(self):
		response = Client().get('/lab-7/friend-list/')
		self.assertEqual(response.status_code, 200)

	def test_get_friend_list_data_url_is_exist(self):
		response = Client().get('/lab-7/get-friend-list/')
		self.assertEqual(response.status_code, 200)

	def test_auth_param_dict(self):
		csui_helper = CSUIhelper()
		auth_param = csui_helper.instance.get_auth_param_dict()
		self.assertEqual(auth_param['client_id'], csui_helper.instance.get_auth_param_dict()['client_id'])

	def test_add_friend(self):
		response_post = Client().post('/lab-7/add-friend/', 
			{'name':"Firandra Savitri", 'npm':"1606829043"}
		)
		self.assertEqual(response_post.status_code, 200)

	def test_validate_npm(self):
		response = self.client.post('/lab-7/validate-npm/')
		html_response = response.content.decode('utf8')
		self.assertEqual(response.status_code,200)
		self.assertJSONEqual(html_response,{'is_taken':False})

	def test_delete_friend(self):
		friend = Friend.objects.create(friend_name="Firandra Savitri", npm="1606829043")
		response = Client().post('/lab-7/friend-list/delete-friend/' + str(friend.id) + '/')
		self.assertEqual(response.status_code,302)
		self.assertNotIn(friend, Friend.objects.all())

	def test_invalid_sso_username_and_password(self):
		username = "firan"
		password = "hahihuheho"
		csui_helper = CSUIhelper()
		with self.assertRaises(Exception) as context:
			csui_helper.instance.get_access_token(username,password)
		self.assertIn("firan",str(context.exception))

	def test_invalid_page_pagination_number(self):
		data = ["haha", "hehe", "hihi", "haha", "hehe", "hihi", "haha", "hehe", "hihi", "haha",
				"hehe", "hihi", "haha", "hehe", "hihi", "haha", "hehe", "hihi", "haha", "hehe",
				"hihi", "haha", "hehe", "hihi", "haha", "hehe", "hihi", "haha", "hehe", "hihi"]
		test_1 = paginate_page("...", data)
		test_2 = paginate_page(-1, data)
		with patch.object(Manager, 'get_or_create') as a:
			a.side_effect = PageNotAnInteger("page number is not an integer")
			res = paginate_page("...", data)
			self.assertEqual(res['page_range'], test_1['page_range'])
		with patch.object(Manager, 'get_or_create') as a:
			a.side_effect = EmptyPage("page number is less than 1")
			res = paginate_page(-1, data)
			self.assertEqual(res['page_range'], test_2['page_range'])
