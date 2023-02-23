from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Giftcarddatailspage:

    def __init__(self, driver):
        self.driver = driver

    # =======main buttons=====
    page_header = (By.XPATH, "(//*[contains(text(),'Please Enter the Details for Your Card')])[2]")


    def getpage_header(self):
        return self.driver.find_element(*Giftcarddatailspage.page_header)









