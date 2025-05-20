from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from course58.gen_funcs.gen_f import ElementActions


class FlightSearch:
    def __init__(self, driver):
        self.driver = driver
        print("In page FlightSearch")



    def search(self, num_of_pass):
        num_pass = self.driver.find_element(By.NAME, 'passCount')
        num_pass1 = Select(num_pass)
        num_pass1.select_by_value(str(num_of_pass))

        # cont = self.driver.find_element(By.NAME, 'findFlights')
        # cont.click()
        element_actions = ElementActions(self.driver)
        element_actions.click_and_report_by_locator((By.NAME, 'findFlights'), "Continue")
        self.handle_popup()

    def handle_popup(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            self.driver.alert.dismiss()
            alert.accept()
            print("Popup handled")
        except:
            print("No popup present")
