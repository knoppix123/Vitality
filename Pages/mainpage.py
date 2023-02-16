from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys




class Mainpage:
    def __init__(self, driver):
        self.driver = driver
    # =======main buttons=====
    mainlogo = (By.XPATH, "//img[@id='logo']")




    def getmainlogo(self):
        return self.driver.find_element(*Mainpage.mainlogo)


    # itemselection = (By.CSS_SELECTOR, "[class='mt-10	text-lg ']")
    #
    #
    #
    # def getitemselection(self):
    #     return self.driver.find_elements(*MenuPage.itemselection)
