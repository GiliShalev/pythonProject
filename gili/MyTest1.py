import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from gili.BaseSelenium import BaseSelenium

class MyTesting(BaseSelenium):

    def __init__(self):
        super().__init__()
    def t1(self):
        driver = super().selenium_init("https://demo.guru99.com/test/newtours/#google_vignette")
        user_name = driver.find_element(By.NAME, "userName")
        user_name.send_keys("tutorial")
        password = driver.find_element(By.NAME, "password")
        password.send_keys("tutorial")
        submit = driver.find_element(By.NAME, "submit")
        submit.click()
        time.sleep(3)
    def t2(self):
        driver = super().selenium_init("https://shop.demoqa.com/my-account/")
    def t3(self):
        driver = super().selenium_init("https://demo.applitools.com/#")
        user_name = driver.find_element(By.ID, "username")
        user_name.send_keys("standard_user")
        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        submit = driver.find_element(By.ID, "log-in")
        submit.click()
        time.sleep(3)
    def t4(self):
        driver = super().selenium_init("https://www.saucedemo.com")
        user_name = driver.find_element(By.ID, "user-name")
        user_name.send_keys("standard_user")
        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        submit = driver.find_element(By.ID, "login-button")
        submit.click()
        time.sleep(3)
        return driver
    def t5(self):
        driver = super().selenium_init("https://www.calculator.net/math - calculator.html")
        financial = driver.find_element(By.PARTIAL_LINK_TEXT, "Financial")
        print("Text is " + financial.text)
        financial = driver.find_element(By.LINK_TEXT, "Financial")
        print("Text is", financial.text)
        financial.click()
    def t6(self):
        driver = super().selenium_init("https://demo.guru99.com/selenium/newtours/reservation.php")
        support = driver.find_element(By.PARTIAL_LINK_TEXT, "SUPPORT")
        support.click()
        time.sleep(3)
    def t7(self):
        driver = super().selenium_init("https://www.calculator.net/math-calculator.html")
        math = driver.find_element(By.CLASS_NAME, "topNavOn")
        if math.text.upper() == 'MATH':
            print("OK")
            print(math.get_attribute("class"))
            print(math.value_of_css_property("cursor"))
        else:
            print("Actual text", math.text)
        time.sleep(3)
    def t8(self):
        driver = super().selenium_init("https://www.demoblaze.com/")
        categories = driver.find_elements(By.ID, "itemc")
        for cat in categories:
            pattern = cat.text
            print(pattern)
            if pattern == 'Phones':
                print('Phones found')
            if "Phones" in cat.text:
                print("IN")

        time.sleep(3)
    def t9(self):
        # Page 28 - Broken link
        driver = super().selenium_init("https://www.phptravels.net/")
    def t10(self):
        driver = self.t4()
        items = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        amount = 0;
        for item in items:
            print(item.text)
            amount = amount + float(item.text.replace("$", ""))

        print("Amount", amount)
        print("Items", len(items))
        print("Average", amount / len(items))
        time.sleep(3)
    def t11(self):
        driver = super().selenium_init("https://www.calculator.net/password-generator.html")
        items = driver.find_elements(By.CLASS_NAME, "cbcontainer")
        items[0].click()
        items[1].click()
        submit = driver.find_element(By.NAME, "submit1")
        submit.click()
        time.sleep(3)
        password = driver.find_element(By.CLASS_NAME, "verybigtext")
        print("Password is:", password.text)
    def t12(self):
        driver = super().selenium_init("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer")
        name = Select(driver.find_element(By.ID, 'userSelect'))
        name.select_by_visible_text("Harry Potter")
        time.sleep(2)
        name.select_by_value("1")
        time.sleep(2)
        name.select_by_index(2)
        time.sleep(3)
    def t13(self):
        driver = self.t4()
        sort = Select(driver.find_element(By.CLASS_NAME, 'product_sort_container'))
        sort.select_by_value("za")
        time.sleep(3)
    def t14(self):
        driver = super().selenium_init("http://www.calculator.net/interest - calculator.html")
        compound = Select(driver.find_element(By.ID, 'ccompound'))
        compound.select_by_value("continuously")
        time.sleep(2)
        compound.select_by_index(0)
        print("Option 1 is:", compound.options[0].text)
        time.sleep(3)
    def t15(self):
        driver = super().selenium_init("http://advantageonlineshopping.com/#/")
        time.sleep(4)
        contact_us = driver.find_element(By.LINK_TEXT, 'CONTACT US')
        contact_us.click()
        categoryListboxContactUs = Select(driver.find_element(By.NAME, 'categoryListboxContactUs'))
        categoryListboxContactUs.select_by_visible_text("Mice")
        productListboxContactUs = Select(driver.find_element(By.NAME, 'productListboxContactUs'))
        productListboxContactUs.select_by_visible_text("HP USB 3 Button Optical Mouse")
        emailContactUs = driver.find_element(By.NAME, 'emailContactUs')
        emailContactUs.send_keys("abcd@gmail.com")
        subjectTextareaContactUs = driver.find_element(By.NAME, 'subjectTextareaContactUs')
        subjectTextareaContactUs.send_keys("Problems")
        send_btn = driver.find_element(By.ID, 'send_btn')
        send_btn.click()
        time.sleep(3)
    def t16(self):
        driver = super().selenium_init("http://advantageonlineshopping.com/#/category/Speakers/4")
        time.sleep(3)
        man = driver.find_element(By.ID, "accordionAttrib1")
        man.click()
        bose = driver.find_element(By.NAME, "manufacturer_0")
        if not bose.is_selected():
            bose.click()
        time.sleep(3)
        if bose.is_selected():
            bose.click()
        time.sleep(3)




myTesting = MyTesting()
#myTesting.t1()
#myTesting.t3()
#myTesting.t4()
#myTesting.t5()
#myTesting.t6()
#myTesting.t7()
#myTesting.t8()
#myTesting.t9()
#myTesting.t10()
#myTesting.t11()
#myTesting.t12()
#myTesting.t13()
#myTesting.t14()
#myTesting.t15()
myTesting.t16()
myTesting.test_end()
