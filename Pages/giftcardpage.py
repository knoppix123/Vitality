from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys




class Giftcardpage:

    def __init__(self, driver):
        self.driver = driver
    # =======main buttons=====
    button_purchase_gift_card = (By.CSS_SELECTOR, "[class='et_pb_button et_pb_button_0 et_hover_enabled et_pb_bg_layout_light']")
    




    def getbutton_purchase_gift_card(self):
        return self.driver.find_element(*Giftcardpage.button_purchase_gift_card)







