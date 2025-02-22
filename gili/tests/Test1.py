from gili.pages.GoogleMain import GoogleMain
from gili.tests.BaseSelenium1 import BaseSelenium1

class TempTests():
    def my_tests(self):
        print ("into test")
        base = BaseSelenium1()
        driver = base.selenium_init("https://www.google.com")
        main = GoogleMain(driver)
        main.search_for_pattern("cat")
        base.test_end()
