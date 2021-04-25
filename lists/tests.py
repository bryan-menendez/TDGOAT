from lists.views import index
from lists.models import Item, List

from django.test import TestCase
from django.urls import resolve
from django.http.request import HttpRequest
from django.template.loader import render_to_string 


class NewItemTest(TestCase):
    def test_can_POST_item_to_existing_list(self):
        our_list = List.objects.create()
        other_list = List.objects.create()

        self.client.post(f'/lists/{our_list.id}/add_item', data={'new_item': "our item comrade"})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "our item comrade")
        self.assertEqual(new_item.list, our_list)

    def test_redirects_to_list_view(self):
        our_list = List.objects.create()
        other_list = List.objects.create()

        response = self.client.post(f'/lists/{our_list.id}/add_item', data={'new_item': "our item comrade"})
        self.assertRedirects(response, f'/lists/{our_list.id}')


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
        newly_created_list = List.objects.first()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/lists/{newly_created_list.id}')
        # self.assertRegex(self.client.current_url, "/lists/view/...") something like that format


class ListViewTest(TestCase):
    def test_passes_correct_list_to_template(self):
        our_list = List.objects.create()
        other_list = List.objects.create()
        response = self.client.get(f'/lists/{our_list.id}')
        self.assertEqual(response.context['list'], our_list)

    def test_uses_list_template(self):
        list_ = List.objects.create()
        response = self.client.get(f"/lists/{list_.id}")
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_display_items_from_unique_list(self):
        our_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=our_list)
        Item.objects.create(text='itemey 2', list=our_list)

        other_list = List.objects.create()
        Item.objects.create(text='bad itemu 1', list=other_list)
        Item.objects.create(text='bad itemu 2', list=other_list)

        response = self.client.get(f'/lists/{our_list.id}')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'bad itemu 1')
        self.assertNotContains(response, 'bad itemu 2')


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'lists/index.html')
