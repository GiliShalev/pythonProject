from selenium.webdriver.common.by import By

class Registration:
    def __init__(self, driver):
        self.driver = driver
        print("In page Login")

    def fill_reg_details(self, first_name, last_name, phone):
        driver = self.driver
        first_name_field = driver.find_element(By.ID, "firstName")
        first_name_field.send_keys(first_name)
        driver.find_element(By.ID, "lastName").send_keys(last_name)
        driver.find_element(By.ID, "userNumber").send_keys(phone)
        driver.find_element(By.XPATH, "//label[@for='gender-radio-1']").click()
        driver.find_element(By.ID, "submit").submit()

