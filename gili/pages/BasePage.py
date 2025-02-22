import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
import pytest

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        print ('into init')
