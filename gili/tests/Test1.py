from gili.pages.GoogleMain import GoogleMain
from gili.tests.BaseSelenium1 import BaseSelenium1

print ("into test")
base = BaseSelenium1()
driver = base.selenium_init("https://www.google.com")
main = GoogleMain(driver)
main.search_for_pattern("cat")
base.test_end()
