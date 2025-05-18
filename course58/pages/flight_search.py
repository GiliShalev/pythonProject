from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from course58.gen_funcs.gen_f import ElementActions


class FlightSearch:
    def __init__(self, driver):
        self.driver = driver
        print("In page FlightSearch")

    def search(self, num_of_pass):
        num_pass = self.driver.find_element(By.NAME, 'passCount')
        num_pass1 = Select(num_pass)
        num_pass1.select_by_value(str(num_of_pass))

        cont = self.driver.find_element(By.NAME, 'findFlights')
        # cont.click()
        element_actions = ElementActions()
        element_actions.click_and_report(cont, "Continue")



