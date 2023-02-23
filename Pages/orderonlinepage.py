from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys




class Orderonlinepage:

    def __init__(self, driver):
        self.driver = driver
    # =======main buttons=====
    search_location_field = (By.CSS_SELECTOR, "[id='location-input']")
    search_location_result = (By.CSS_SELECTOR, "[class='mbaa']")
    button_search = (By.CSS_SELECTOR, "[aria-label='Search']")
    select_alpharetta_location = (By.CSS_SELECTOR, "[id='10492-name']")
    select_pickup = (By.CSS_SELECTOR, "[class='btn-lg btn btn-default default btn-block']")
    select_the_love_bowl = (By.XPATH, "//h4[contains(text(),'The Love Bowl')]")
    button_add_to_bag = (By.CSS_SELECTOR, "[class='btn btn-block btn-primary add-to-cart']")
    button_open_bag = (By.CSS_SELECTOR), "[class='nav navbar-nav navbar-right navbar-cart hidden-xs']"


    def getsearch_location_field(self):
        return self.driver.find_element(*Orderonlinepage.search_location_field)
    def getsearch_location_result(self):
        return self.driver.find_element(*Orderonlinepage.search_location_result)
    def getbutton_search(self):
        return self.driver.find_element(*Orderonlinepage.button_search)
    def getalpharetta_location(self):
        return self.driver.find_element(*Orderonlinepage.select_alpharetta_location)
    def getselect_pickup(self):
        return self.driver.find_element(*Orderonlinepage.select_pickup)
    def getselect_the_love_bowl(self):
        return self.driver.find_element(*Orderonlinepage.select_the_love_bowl)
    def getbutton_add_to_bag(self):
        return self.driver.find_element(*Orderonlinepage.button_add_to_bag)
    def getbutton_open_bag(self):
        return self.driver.find_element(*Orderonlinepage.button_open_bag)




