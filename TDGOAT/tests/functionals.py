from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_can_start_list_and_retrieve_later(self):
        self.browser.get("http://localhost:8000")
        
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
        time.sleep(1)
        
        #try adding a second item
        box_new_item = self.browser.find_element_by_id("box_new_item")
        box_new_item.send_keys('Use Peacock')
        box_new_item.send_keys(Keys.ENTER)
        time.sleep(1)
        
        table = self.browser.find_element_by_id("table_todo_list")
        rows = table.find_elements_by_tag_name("tr")
        
        #check that all input was stored
        self.assertIn('Buy peacock feathers', [row.text for row in rows])
        self.assertIn('Use Peacock', [row.text for row in rows])
        

    def tearDown(self):
        self.browser.quit()
        
if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    