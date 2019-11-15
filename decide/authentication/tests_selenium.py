import unittest
from selenium import webdriver

class TestSignup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test_signup_fire(self):
        self.driver.get("http://localhost:5000/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("practica")
        self.driver.find_element_by_id('id_password').send_keys("practica")
        self.driver.find_element_by_id('login-form').click()
        self.assertTrue(len(self.driver.find_elements_by_id('user-tools'))>0) 
    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()
