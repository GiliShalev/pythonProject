import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
import pytest

from gili.tests.gen_funcs import GenFuncs


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        print('\nIn set up class')

    def setUp(self):
        print('\nIn set up')

    def test_blaze(self):
        driver = self.driver
        driver.get("https://www.demoblaze.com/")
        all_cat = driver.find_elements(By.ID, "itemc")
        print("Num of cat: " + str(len(all_cat)))
        phone_exist = False
        for cat in all_cat:
            if cat.text == 'Phones':
                phone_exist = True
                print('Phones is in the list')

            print(cat.text)

        if not phone_exist:
            print('Phones is not in the list')




    def test_google(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        time.sleep(2)
        search_field = driver.find_element(By.NAME, "q")
        search_field.clear()
        search_field.send_keys("Cat")

        # ok = driver.find_element(By.NAME, "btnK")
        # ok.click()

        time.sleep(2)
        print("In test1")

    def test_yahoo(self):
        print("In test2")




    def test_tools(self):
        driver = self.driver
        driver.get('https://demoqa.com/login')
        user_name = driver.find_element(By.ID, 'userName')
        password = driver.find_element(By.ID, 'password')
        login = driver.find_element(By.ID, 'login')

        user_name.send_keys('tutorial')
        password.send_keys('tutorial')
        time.sleep(2)
        login.click()

    def test_flight(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/test/newtours/#google_vignette")
        user_name = driver.find_element(By.NAME, 'userName')
        password = driver.find_element(By.NAME, 'password')
        submit = driver.find_element(By.NAME, 'submit')

        user_name.send_keys('tutorial')
        password.send_keys('tutorial')
        submit.click()

    def test_calculator(self):
        driver = self.driver
        driver.get('https://www.calculator.net/math-calculator.html')
        financial = driver.find_element(By.LINK_TEXT, 'FINANCIAL')
        print(financial.text)


    def test_pass_gen(self):
        driver = self.driver
        driver.get('https://www.calculator.net/password-generator.html')
        time.sleep(3)
        include_lower_case = driver.find_element(By.ID, 'inumber')
        if not include_lower_case.is_selected():
            include_lower_case.click()
        a = 9

    def test_swag_labs(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com/inventory.html')
        # Login
        user_name = driver.find_element(By.ID, "user-name")
        user_name.send_keys("standard_user")
        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        submit = driver.find_element(By.ID, "login-button")
        submit.click()
        time.sleep(3)

        # Inventory page
        all_prices = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
        for price in all_prices:
            print(price.text[1:])

    def test_customer(self):
        self.driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer")
        combo_box = self.driver.find_element(By.ID, 'userSelect')
        select = Select(combo_box)
        select.select_by_visible_text("Harry Potter")
        time.sleep(2)
        select.select_by_index(0)
        time.sleep(2)
        select.select_by_value('1')
        time.sleep(2)

    def tearDown(self):
        print('In tear down')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('In tear down class')

    def test_order_flight(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/test/newtours/#google_vignette")
        gen_funcs = GenFuncs(driver)
        gen_funcs.select_category("Flights")
        time.sleep(3)

        # Handle radio button
        trip_type = driver.find_elements(By.NAME, "tripType")
        for trip in trip_type:
            if trip.get_attribute("value") == "oneway":
                trip.click()
                break

        time.sleep(3)

        # Combo box
        num_of_pass = driver.find_element(By.NAME, 'passCount')
        select_num_of_pass = Select(num_of_pass)
        select_num_of_pass.select_by_visible_text("3")
        time.sleep(3)






