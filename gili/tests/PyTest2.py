from unittest import skip

import pytest

from gili.pages.GoogleMain import GoogleMain
from gili.tests.BaseTest import BaseTest
class MyTestCase(BaseTest):

    def test_something(self):
        print('In test 1')
        self.driver.get("https://www.google.com")
        main = GoogleMain(self.driver)
        main.search_for_pattern("cat")
    #@pytest.mark.skip
    def test_something1(self):
        print('In test 2')
        self.driver.get("https://www.google.com")
        main = GoogleMain(self.driver)
        main.search_for_pattern("cat")



