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
    button_main = ( By.CSS_SELECTOR, "[class='test menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-98']")
    button_store_locations = (By.CSS_SELECTOR, "[id='menu-item-135']")
    button_catering = (By.CSS_SELECTOR, "[id='menu-item-871']")
    button_loyalty_program = (By.CSS_SELECTOR, "[id='menu-item-3908']")
    button_gift_cards = (By.CSS_SELECTOR, "[id='menu-item-3888']")
    button_about = (By.CSS_SELECTOR, "[id='menu-item-136']")
    button_franchise = (By.CSS_SELECTOR, "[id='menu-item-1646']")
    button_order_now = (By.CSS_SELECTOR, "[id='menu-item-10638']")

    def getmainlogo(self):
        return self.driver.find_element(*Mainpage.mainlogo)
    def getbutton_menu(self):
        return self.driver.find_element(*Mainpage.button_main)
    def getbutton_store_locations(self):
        return self.driver.find_element(*Mainpage.button_store_locations)
    def getbutton_catering(self):
        return self.driver.find_element(*Mainpage.button_catering)
    def getbutton_loyalty_program(self):
        return self.driver.find_element(*Mainpage.button_loyalty_program)
    def getbutton_gift_cards(self):
        return self.driver.find_element(*Mainpage.button_gift_cards)
    def getbutton_about(self):
        return self.driver.find_element(*Mainpage.button_about)
    def getbutton_franchise(self):
        return self.driver.find_element(*Mainpage.button_franchise)
    def getbutton_order_now(self):
        return self.driver.find_element(*Mainpage.button_order_now)







    # itemselection = (By.CSS_SELECTOR, "[class='mt-10	text-lg ']")
    #
    #
    #
    # def getitemselection(self):
    #     return self.driver.find_elements(*MenuPage.itemselection)
