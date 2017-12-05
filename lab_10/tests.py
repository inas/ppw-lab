from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .custom_auth import auth_login, auth_logout
from .csui_helper import get_access_token
import environ

root = environ.Path(__file__) - 2 # two folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')


class Lab10UnitTest(TestCase):
	def test_lab_10_url_is_exist(self):
		response = Client().get('/lab-10/')
		self.assertEqual(response.status_code, 200)

	def setUp(self):
		self.username = env("SSO_USERNAME")
		self.password = env("SSO_PASSWORD")

	def test_lab_9_page_when_user_is_logged_in_or_not(self):
		#not logged in, render login template
		response = self.client.get('/lab-10/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed('lab_10/login.html')

		#logged in, redirect to dashboard page
		self.client.post('/lab-10/custom_auth/login/', {'username': self.username, 'password': self.password})
		response = self.client.get('/lab-10/')
		self.assertEqual(response.status_code, 302)
		self.assertTemplateUsed('lab_10/dashboard.html')

	def test_direct_access_to_dashboard_url(self):
		#not logged in, redirect to login page
		response = self.client.get('/lab-10/dashboard/')
		self.assertEqual(response.status_code, 302)

		#logged in, render dashboard template
		response = self.client.post('/lab-10/custom_auth/login/', {'username': self.username, 'password': self.password})
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/dashboard/')
		self.assertEqual(response.status_code, 200)


	def test_log_in_false(self):
		#not logged in, render login template
		response =Client().get('/lab-10/')
		self.assertTemplateUsed('lab_10/login.html')

		#logged in, redirect to profile page
		response = Client().post('/lab-10/custom_auth/login/', {'username': "apa", 'password': "iya"})
		self.assertEqual(response.status_code, 302)
		self.assertTemplateUsed('lab_10/login.html')

	def test_logout(self):
		response = self.client.post('/lab-10/custom_auth/login/', {'username': self.username, 'password': self.password})
		self.assertEqual(response.status_code, 302)
		response = self.client.post('/lab-10/custom_auth/logout/')
		html_response = self.client.get('/lab-10/').content.decode('utf-8')
		self.assertEqual(response.status_code, 302)

	def test_movie_list_page(self):
		#test if list page is accessible when user is not logged in
		response = self.client.get('/lab-10/movie/list/')
		self.assertEqual(response.status_code, 200)
		#self.assertFalse(response.context['login'])

		#test if user is able to get movie list when logged in
		response = self.client.post('/lab-10/custom_auth/login/', {'username': self.username, 'password': self.password})
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/movie/list/')
		self.assertEqual(response.status_code, 200)
		response = self.client.get('/lab-10/movie/list/', {'judul':'Dunkirk', 'tahun':'2017'})
		self.assertEqual(response.status_code, 200)

	def test_movie_details_page(self):
		#user can still access details whether they are not logged in or not
		response = self.client.get('/lab-10/movie/detail/tt4046784/')
		self.assertEqual(response.status_code, 200)

		#logged in
		response = self.client.post('/lab-10/custom_auth/login/', {'username': self.username, 'password': self.password})
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/dashboard/')
		self.assertEqual(response.status_code, 200)
		response = self.client.get('/lab-10/movie/detail/tt5013056/')
		self.assertEqual(response.status_code, 200)

	def test_add_movie_to_watch_later(self):
		#not logged in
		response = self.client.get('/lab-10/movie/watch_later/add/tt5013056/')
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/movie/watch_later/add/tt3315342/')
		self.assertEqual(response.status_code, 302)

		#manual adding, check duplicates on session
		response = self.client.get('/lab-10/movie/watch_later/add/tt3315342/')
		html_response = self.client.get('/lab-10/movie/detail/tt3315342/').content.decode('utf-8')
		# self.assertIn("Movie already exist on SESSION! Hacking detected!", html_response)

		#logged in
		response = self.client.post('/lab-10/custom_auth/login/', {'username': self.username, 'password': self.password})
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/dashboard/')
		self.assertEqual(response.status_code, 200)
		#same as session movie
		response = self.client.get('/lab-10/movie/watch_later/add/tt5013056/')
		self.assertEqual(response.status_code, 302)
		#different movie
		response = self.client.get('/lab-10/movie/watch_later/add/tt2283362/')
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/movie/watch_later/add/tt0458339/')
		self.assertEqual(response.status_code, 302)

		#manual adding
		response = self.client.get('/lab-10/movie/watch_later/add/tt2283362/')
		html_response = self.client.get('/lab-10/movie/detail/tt2283362/').content.decode('utf-8')
		# self.assertIn("Movie already exist on DATABASE! Hacking detected!", html_response)

	def test_watch_later_movie_page_when_user_is_logged_in_and_otherwise(self):
		#not logged in
		response = self.client.get('/lab-10/movie/watch_later/add/tt3896198/')
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/movie/watch_later/add/tt1790809/')
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/movie/watch_later/')
		self.assertEqual(response.status_code, 200)

		#logged in
		response = self.client.post('/lab-10/custom_auth/login/', {'username': self.username, 'password': self.password})
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/dashboard/')
		self.assertEqual(response.status_code, 200)
		response = self.client.get('/lab-10/movie/watch_later/add/tt2015381/')
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/movie/watch_later/add/tt6342474/')
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/movie/watch_later/')
		self.assertEqual(response.status_code, 200)
		#self.assertTrue(response.context['login'])

	def test_api_search_movie(self):
		#init search
		response = Client().get('/lab-10/api/movie/-/-/')
		self.assertEqual(response.status_code, 200)
		#search movie by title
		response = Client().get('/lab-10/api/movie/Dunkirk/-/')
		self.assertEqual(response.status_code, 200)
		#search movie by title and year
		response = Client().get('/lab-10/api/movie/Dunkirk/2017/')
		self.assertEqual(response.status_code, 200)
		# 0 > number of result <= 3
		response = Client().get('/lab-10/api/movie/it/2017/')
		self.assertEqual(response.status_code, 200)
		#not found
		response = Client().get('/lab-10/api/movie/click/-/')
		self.assertEqual(response.status_code, 200)

