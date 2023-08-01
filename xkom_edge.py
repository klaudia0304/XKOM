from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
import pytest


#Creating a class
class ViewTheVideo(unittest.TestCase):
    #creating a method/function
    def setUp(self):
        self.driver=webdriver.Edge() #define the driver
        self.driver.maximize_window()
        self.driver.get("https://www.x-kom.pl/unbox")
        sleep(3)
    def testViewVideo(self):
        coockie_accept_btn=self.driver.find_element(By.XPATH, "//button[@class='sc-15ih3hi-0 sc-1p1bjrl-9 dRLEBj']")
        coockie_accept_btn.click()
        sleep(3)
        sprawdz_box=self.driver.find_element(By.XPATH, "//div[@class='sc-fzoLsD dAZHqx']//div[text()='Sprawdź swoje boxy']")
        sprawdz_box.click()
        sleep(3)
        otworz_box=self.driver.find_element(By.XPATH, "//div[@class='sc-fzoLsD dAZHqx']//div[text()='Otwórz']")
        otworz_box.click()
        sleep(5)
        losuj=self.driver.find_element(By.XPATH, "//div[@class='sc-fzoLsD dAZHqx']//div[text()='Losuj']")
        losuj.click()
        sleep(60)
