from lists.views import index
from lists.models import Item

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
        
        
class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'first item ever'
        first_item.save()
        
        second_item = Item()
        second_item.text = 'item the second'
        second_item.save()
        
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        
        first_saved = saved_items[0]
        second_saved = saved_items[1]
        
        self.assertEqual(first_saved.text, 'first item ever')
        self.assertEqual(second_saved.text, 'item the second')
        
    def test_can_save_POST_request(self):
        self.client.post('/', data={'new_item' : 'a new item'})
        
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'a new item')
        
        
    def test_redirect_after_post(self):
        response = self.client.post('/', data={'new_item' : 'a new item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')
        
    def test_only_save_on_post(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)
        
    def test_display_all_items(self):
        Item.objects.create(text="item 1")
        Item.objects.create(text="item 2")
        
        response = self.client.get("/")
        
        self.assertIn("item 1", response.content.decode())
        self.assertIn("item 2", response.content.decode())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        