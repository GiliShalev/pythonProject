import time
import unittest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

from course58.pages.flight_search import FlightSearch
from course58.pages.flight_search_result import FlightSearchResult
from course58.pages.login import Login


class Sanity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)
        print('\nSetUpClass')

    def test_order_flight(self):
        driver = self.driver
        driver.get('https://demo.guru99.com/test/newtours/')

        login = Login(driver)
        login.navigate("Flights")

        flight_search = FlightSearch(driver)
        flight_search.search(4)

        result = FlightSearchResult(driver)
        result.print_msg()

    def setUp(self):
        print('SetUp')








    def tearDown(self):
        print('TearDown')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print('tearDownClass')



