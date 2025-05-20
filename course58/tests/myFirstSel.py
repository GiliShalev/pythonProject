import time
import unittest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from course58.pages.flight_search import FlightSearch
from course58.pages.flight_search_result import FlightSearchResult
from course58.pages.login import Login
from course58.pages.registration import Registration


class Sanity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)
        print('\nSetUpClass')

    def test_flight_login(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/test/newtours/#google_vignette")
        user_name = driver.find_element(By.NAME, 'userName')
        password = driver.find_element(By.NAME, 'password')
        submit = driver.find_element(By.NAME, 'submit')

        user_name.send_keys('tutorial')
        password.send_keys('tutorial')
        submit.click()

        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "OK")))
            print("OK button is clickable")
        except TimeoutException:
            print("OK button not found or not clickable - timeout")

    def test_reg_regular(self):
        driver = self.driver
        driver.get('https://demoqa.com/automation-practice-form')
        registration = Registration(driver)
        registration.fill_reg_details("Gili", "Shalev", "0547533422")

    def test_reg_admin(self):
        driver = self.driver
        driver.get('https://demoqa.com/automation-practice-form')
        registration = Registration(driver)
        registration.fill_reg_details("Yogev", "Shalev", "0547533423")

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



