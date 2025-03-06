from selenium.webdriver.common.by import By


class GenFuncs:
    def __init__(self, driver):
        self.driver = driver
    def select_category(self, text):
        a = 99
        driver = self.driver
        cat = driver.find_element(By.LINK_TEXT, text)
        cat.click()