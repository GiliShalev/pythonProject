class ElementActions:

    def click_and_report(self, elem, name):
        elem.click()
        print(" Clicking " + name)