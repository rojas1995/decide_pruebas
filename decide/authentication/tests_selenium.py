import unittest
from selenium import webdriver
from django.contrib.auth.models import User

class TestSignup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        
        u2 = User(username='admin')
        u2.set_password('admin')
        u2.is_superuser = True
        u2.save()


    def test_signup_fire(self):
        self.driver.get("http://localhost:5000/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("admin")
        self.driver.find_element_by_id('id_password').send_keys("admin")
        self.driver.find_element_by_id('login-form').click()
        self.assertTrue(len(self.driver.find_elements_by_id('user-tools'))>0) 
    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()
