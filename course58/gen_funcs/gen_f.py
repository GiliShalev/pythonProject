class ElementActions:
    def __init__(self, driver):
        self.driver = driver

    def click_and_report(self, elem, name):
        elem.click()
        print(" Clicking " + name)

    def click_and_report_by_locator(self, locator, name):
        elem = self.driver.find_element(locator[0], locator[1])
        elem.click()
        print(" Clicking " + name)



class Car:
    def __init__(self, model, vendor):
        self.model = model
        self.vendor = vendor
