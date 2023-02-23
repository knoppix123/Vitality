from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Giftcardpage2:

    def __init__(self, driver):
        self.driver = driver

    # =======main buttons=====
    button_purchase_gift_card2 = (By.XPATH, "(//*[@class='menu-button'])[1]")
    button_check_balance = (By.XPATH, "(//*[@class='menu-button'])[2]")
    button_check_order_status = (By.XPATH, "(//*[@class='menu-button'])[3]")


    def getbutton_purchase_gift_card2(self):
        return self.driver.find_element(*Giftcardpage2.button_purchase_gift_card2)
    def getbutton_check_balance(self):
        return self.driver.find_element(*Giftcardpage2.button_check_balance)
    def getbutton_check_order_status(self):
        return self.driver.find_element(*Giftcardpage2.button_check_order_status)








