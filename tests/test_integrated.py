import unittest
import time
from flask import url_for
from urllib.request import urlopen
from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db, bcrypt
from application.models import Cheeses, Wines, Pairing


# Create TestBase
class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DATABASE'))
        app.config['SECRET_KEY'] = getenv('SKEY')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/michaela6543/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

## Test add functionality

class TestAdd(TestBase):
    def test_add(self):
        """
        Test that a user can add a Cheese to the database
        """
        
        # Click "Add Cheese" link in navigation bar
        self.driver.find_element_by_xpath("/html/body/a[2]").click()
        time.sleep(1)

        #Fill in Cheese form
        self.driver.find_element_by_xpath("//*[@id="cheese_name"]").send_keys(name)
        self.driver.find_element_by_xpath("//*[@id="cheese_texture"]").send_keys(texture)
        self.driver.find_element_by_xpath("//*[@id="cheese_origin"]").send_keys(origin)
        self.driver.find_element_by_xpath("//*[@id="cheese_aroma"]").send_keys(aroma)
        self.driver.find_element_by_xpath("//*[@id="cheese_taste"]").send_keys(taste)
        self.driver.find_element_by_xpath("//*[@id="submit"]").click()
        time.sleep(1)
        
        #assert browser redirection to index page
        assert url_for('index') in self.driver.current_url

if __name__=='__main__':
    unittest.main(port=5000)
