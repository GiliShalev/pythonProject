import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
import pytest

class BaseTest(unittest.TestCase):

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
        #service = ChromeService(executable_path=ChromeDriverManager().install())
        #driver = webdriver.Chrome(service=service)
        #driver.implicitly_wait(10)
        #driver.maximize_window()
        #self.driver = driver
    def tearDown(self):
        print('In tear down')
        #self.driver.close()

    @classmethod
    def tearDownClass(cls):
        print('In tear down class')
        cls.driver.close()


