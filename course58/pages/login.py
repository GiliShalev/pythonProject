from selenium.webdriver.common.by import By

class Login:
    def __init__(self, driver):
        self.driver = driver
        print("In page Login")

    def navigate(self, text):
        flights = self.driver.find_element(By.LINK_TEXT, text)
        print("Clicking " + text)
        flights.click()