from unittest import skip
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

from gili.pages.GoogleMain import GoogleMain
from gili.tests.BaseTest import BaseTest
class MyTestCase2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('In set up class')
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(10)
        driver.maximize_window()
        cls.driver = driver

    def setUp(self):
        print('\nIn set up')
        # service = ChromeService(executable_path=ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=service)
        # driver.implicitly_wait(10)
        # driver.maximize_window()
        # self.driver = driver

    def tearDown(self):
        print('In tear down')
        # self.driver.close()

    @classmethod
    def tearDownClass(cls):
        print('In tear down class')
        cls.driver.close()

    def test_something(self):
        print('In test 1')
        self.driver.get("https://www.google.com")
        main = GoogleMain(self.driver)
        main.search_for_pattern("cat")
    #@pytest.mark.skip
    def test_something1(self):
        print('In test 2')
        self.driver.get("https://www.google.com")
        main = GoogleMain(self.driver)
        main.search_for_pattern("cat")



