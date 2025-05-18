from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class FlightSearchResult:
    def __init__(self, driver):
        self.driver = driver
        print("In page FlightSearchResult")

    def print_msg(self):
        msg = self.driver.find_element(By.XPATH, "//font[@size='4']")
        print(msg.text)
