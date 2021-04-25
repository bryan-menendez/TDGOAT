from lists.views import index
from lists.models import Item, List

from django.test import TestCase
from django.urls import resolve
from django.http.request import HttpRequest
from django.template.loader import render_to_string 


class ListAndItemModelsTest(TestCase):
    def test_saving_and_retrieving_items(self):
        new_list = List()
        new_list.save()

        first_item = Item()
        first_item.text = "first"
        first_item.list = new_list
        first_item.save()

        second_item = Item()
        second_item.text = "second"
        second_item.list = new_list
        second_item.save()

        # are the items saved?
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        # is the list itself saved?
        saved_list = List.objects.first()
        self.assertEqual(saved_list, new_list)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, "first")
        self.assertEqual(first_saved_item.list, new_list)
        self.assertEqual(second_saved_item.text, "second")
        self.assertEqual(second_saved_item.list, new_list)


class NewListTest(TestCase):
    def test_can_save_POST_request(self):
        self.client.post('/lists/new', data={'new_item': 'a new item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'a new item')

    def test_redirect_after_post(self):
        response = self.client.post('/lists/new', data={'new_item': 'a new item'})
        self.assertEqual(response.status_code, 302)
        # self.assertRegex(self.client.current_url, "/lists/view/...") something like that format


class ListViewTest(TestCase):
    def test_uses_list_template(self):
        response = self.client.get("/lists/the-one-and-only-forever-and-ever-till-the-end-of-time")
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_displays_all_items(self):
        list_ = List.objects.create()
        Item.objects.create(text='itemey 1', list=list_)
        Item.objects.create(text='itemey 2', list=list_)

        response = self.client.get('/lists/the-one-and-only-forever-and-ever-till-the-end-of-time')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'lists/index.html')
