import time
import unittest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

class Sanity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)
        print('\nSetUpClass')

    def setUp(self):
        print('SetUp')

    def test_google(self):
        driver = self.driver
        driver.get('https://google.com')

        # search_field = driver.find_element(By.NAME, 'xxx')
        # search_field = driver.find_element(By.ID, 'xxx')
        # search_field = driver.find_element(By.LINK_TEXT, 'Gmail')
        # search_field = driver.find_element(By.PARTIAL_LINK_TEXT, 'Gmail')
        # search_field = driver.find_element(By.CLASS_NAME, 'gb_X')
        # search_field = driver.find_element(By.TAG_NAME, 'input')
        # search_field = driver.find_element(By.XPATH, 'input')
        # search_field = driver.find_element(By.CSS_SELECTOR, 'input')




        search_field = driver.find_element(By.CLASS_NAME, 'gLFyf')
        val = search_field.get_attribute('id')
        print("ID is " + val)
        search_field.send_keys('Cat')
        search_field.send_keys(Keys.ENTER)
        search_field.click()
        # Locate the GOOGLE home image and click it

        time.sleep(8)
        print("Test1")

    def test_google_1(self):
        print("Test2")

    def test_tools_qa(self):
        self.driver.get("https://demoqa.com/login")

        new_user = self.driver.find_element(By.ID, 'newUser')
        print(new_user.get_attribute('type'))

        user_name = self.driver.find_element(By.ID, 'userName')
        password = self.driver.find_element(By.ID, 'password')
        login = self.driver.find_element(By.ID, 'login')

        user_name.send_keys('aaaa')
        password.send_keys('bbb')
        login.click()
        time.sleep(5)

    def test_calc(self):
        self.driver.get("https://www.calculator.net/math-calculator.html")
        l1 = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Financial')
        print("Text is: " + l1.text)
        l1.click()
        time.sleep(5)

    def test_calc_links(self):
        self.driver.get("https://www.calculator.net/math-calculator.html")
        all_links = self.driver.find_elements(By.TAG_NAME, 'a')
        print(len(all_links))
        for link in all_links:
            # Print like that: Link 1: text... (Only for links that has text)
            print(link.get_attribute('href'))
            print(link.text)

    def test_xyz_bank(self):
        self.driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer")
        sel = self.driver.find_element(By.NAME, 'userSelect')
        select = Select(sel)
        select.select_by_index(0)
        select.select_by_value('2')
        select.select_by_visible_text("Harry Potter")
        time.sleep(3)

    def tearDown(self):
        print('TearDown')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print('tearDownClass')



