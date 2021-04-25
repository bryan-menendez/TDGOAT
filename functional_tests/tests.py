import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from django.test import LiveServerTestCase
from django.test import TestCase
from lists.models import Item

MAX_WAIT = 3


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve_later(self):
        self.browser.get(self.live_server_url)

        # test adding an item
        box_new_item = self.browser.find_element_by_id("box_new_item")
        box_new_item.send_keys('Buy peacock feathers')
        box_new_item.send_keys(Keys.ENTER)
        self.wait_search_for_item_row_in_table("1: Buy peacock feathers")

        # try adding a second item
        box_new_item = self.browser.find_element_by_id("box_new_item")
        box_new_item.send_keys('Use Peacock')
        box_new_item.send_keys(Keys.ENTER)
        self.wait_search_for_item_row_in_table('2: Use Peacock')

    def test_can_start_list_for_several_users(self):
        # start user A's session
        self.browser.get(self.live_server_url)

        # user A adds an item to a list
        box_new_item = self.browser.find_element_by_id("box_new_item")
        box_new_item.send_keys('Buy peacock feathers')
        box_new_item.send_keys(Keys.ENTER)
        self.wait_search_for_item_row_in_table("1: Buy peacock feathers")

        # action generates a list A with a unique id
        list_url_the_first = self.browser.current_url
        self.assertRegex(list_url_the_first, '/lists/.+')

        # lets create a user B
        # restart browser and generate a new session
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # user B visits the homepage and sees a different list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # user b starts a new list by entering a new item
        box_new_item = self.browser.find_element_by_id("box_new_item")
        box_new_item.send_keys('arigato mister roboto')
        box_new_item.send_keys(Keys.ENTER)
        self.wait_search_for_item_row_in_table('1: arigato mister roboto')

        # user b adds a 2nd item to the list
        box_new_item = self.browser.find_element_by_id("box_new_item")
        box_new_item.send_keys('TUETUEEEEEEEEEE')
        box_new_item.send_keys(Keys.ENTER)
        self.wait_search_for_item_row_in_table("2: TUETUEEEEEEEEEE")

        # user b gets a link to his list
        # it must be a different link that user A's list
        list_url_the_second = self.browser.current_url
        self.assertNotEqual(list_url_the_first, list_url_the_second)

        # if we go to users A list, it still exists
        self.browser.get(list_url_the_first)
        self.wait_search_for_item_row_in_table('1: Buy peacock feathers')

    def wait_search_for_item_row_in_table(self, row_text):
        start_time = time.time()

        while True:
            try:
                table = self.browser.find_element_by_id('table_todo_list')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)