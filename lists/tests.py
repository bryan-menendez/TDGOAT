from django.test import TestCase
from django.urls import resolve

from lists.views import index


class SmokeTest(TestCase):
    def test_bad_smoke(self):
        self.assertEqual(2+1, 3)
        
    def test_root_url_resolves_to_index_page(self):
        found = resolve('/')
        self.assertEqual(found.func, index)