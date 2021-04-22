from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_can_start_list_and_retrieve_later(self):
        self.browser.get("http://localhost:8000")
        
        self.assertIn("to-do", self.browser.title)
        self.fail("finish test")

    def tearDown(self):
        self.browser.quit()
        
if __name__ == '__main__':
    unittest.main()