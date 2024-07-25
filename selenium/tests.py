import os
import pathlib
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()
    
options = webdriver.ChromeOptions()
service = Service(executable_path="C:/Users/User/OneDrive/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_id("increase")
        increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "1")

    def test_decrease(self):
        driver.get(file_uri("counter.html"))
        decrease = driver.find_element_by_id("decrease")
        decrease.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "-1")

    def test_multiple_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_id("increase")
        for i in range(5):
            increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "5")

    def test_multiple_decrease(self):
        driver.get(file_uri("counter.html"))
        decrease = driver.find_element_by_id("decrease")
        for i in range(-5):
            decrease.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "-5")
