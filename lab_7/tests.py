from django.test import TestCase
from .views import index
from django.test import Client
from django.urls import resolve
# Create your tests here.
class Lab6UnitTest(TestCase):

    def test_lab_6_url_is_exist(self):
        response = Client().get('/lab-7/')
        self.assertEqual(response.status_code, 200)

    def test_lab6_using_index_func(self):
        found = resolve('/lab-7/')
        self.assertEqual(found.func, index)
