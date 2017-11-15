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


	def test_add_friend(self):
		response_post = Client().post('/lab-7/add-friend/', {'name':"AII", 'npm':"1606829730"})
		counting_all_friend = Friend.objects.all().count()
		self.assertEqual(counting_all_friend, 1)

	def test_add_existing_friend(self):
		response_post = Client().post('/lab-7/add-friend/', {'name':"AII", 'npm':"1606829730"})
		counting_all_friend = Friend.objects.all().count()
		response_post = Client().post('/lab-7/add-friend/', {'name':"AII", 'npm':"1606829730"})
		self.assertEqual(counting_all_friend, 1)        

	def test_delete_friend(self):
		friend = Friend.objects.create(friend_name="AII", npm="1606829730")
		response = Client().post('/lab-7/friend-list/delete-friend/' + str(friend.id) + '/')
		self.assertEqual(response.status_code,302)
		self.assertNotIn(friend, Friend.objects.all())

	def test_invalid_sso(self):
		username = "username"
		password = "password"
		csui_helper = CSUIhelper()
		with self.assertRaises(Exception) as context:
			csui_helper.instance.get_access_token(username,password)
		self.assertIn("username",str(context.exception))

	def test_pagination(self):
		data = ["1","2","3","4"]
		test1 = paginate_page("...", data)
		test2 = paginate_page(-1, data)
		with patch.object(Manager, 'get_or_create') as a:
			a.side_effect = PageNotAnInteger("page is not an integer")
			res = paginate_page("...", data)
			self.assertEqual(res['page_range'], test1['page_range'])
		with patch.object(Manager, 'get_or_create') as a:
			a.side_effect = EmptyPage("page number is less than 1")
			res = paginate_page(-1, data)
			self.assertEqual(res['page_range'], test2['page_range'])
