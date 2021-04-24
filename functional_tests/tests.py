from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from django.test import LiveServerTestCase
import time 
import unittest
from pip._vendor.retrying import MAX_WAIT

MAX_WAIT = 3

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_can_start_list_and_retrieve_later(self):
        self.browser.get(self.live_server_url)
        
        #check proper tags and names
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn('To-Do', header_text)
        
        box_new_item = self.browser.find_element_by_id("box_new_item")
        self.assertEqual(
            box_new_item.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        
        #test adding an item
        box_new_item.send_keys('Buy peacock feathers')
        box_new_item.send_keys(Keys.ENTER)
        self.wait_for_row_in_table('Buy peacock feathers')
        
        #try adding a second item
        box_new_item = self.browser.find_element_by_id("box_new_item")
        box_new_item.send_keys('Use Peacock')
        box_new_item.send_keys(Keys.ENTER)
        self.wait_for_row_in_table('Use Peacock')
        
        
    def tearDown(self):
        self.browser.quit()
        
    def wait_for_row_in_table(self, row_text):
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    