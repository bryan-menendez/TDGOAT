from lists.views import index

from django.test import TestCase
from django.urls import resolve
from django.http.request import HttpRequest
from django.template.loader import render_to_string 

class SmokeTest(TestCase):
    def test_bad_smoke(self):
        self.assertEqual(2+1, 3)        
        
    # def test_index_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = index(request)
    #     html = response.content.decode('utf8')
    #     self.assertTrue(html.strip().startswith('<html>'))
    #     self.assertTrue(html.strip().endswith('</html>'))
    #
    # def test_home_page_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = index(request)
    #     html = response.content.decode()
    #     expected_html = render_to_string('lists/index.html')
    #     self.assertEqual(html, expected_html)

class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'lists/index.html')
        
    def test_can_save_post_request(self):
        response = self.client.post('/', data={'new_item' : 'A new list item of death'})
        self.assertIn('A new list item of death', response.content.decode())
        self.assertTemplateUsed(response, 'lists/index.html')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        