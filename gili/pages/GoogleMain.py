from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from gili.pages.BasePage import BasePage
from gili.pages.Locators import MainPageLocators


class GoogleMain(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    def search_for_pattern(self,pattern):
        print ('into search for pattern')
        search = MainPageLocators().SEARCH
        #search = self.driver.find_element(search[0], search[1])
        search = self.driver.find_element(By.NAME, "q")
        search.click()
        search.clear()
        search.send_keys(pattern)
        search.send_keys(Keys.ENTER)