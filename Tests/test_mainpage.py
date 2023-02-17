
import pytest
from selenium import webdriver
import time
from Utilities.BaseClass import BaseClass
from Pages.mainpage import Mainpage
import selenium.common.exceptions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

#
# @pytest.fixture(params=customerdata.test_customer_data)
# def getData(request):
#     return request.param

class Testmenuitems(BaseClass):

    def test_top_menu_buttons(self):
        HP = Mainpage(self.driver)
        HP.getmainlogo()
        time.sleep(2)

        HP.getbutton_menu().click()
        title = self.driver.title
        print(title)
        assert title == "Our Menu | Açaí Bowls | Vitality Bowls"
        HP.getmainlogo().click()

        HP.getbutton_store_locations().click()
        title = self.driver.title
        assert title == "Store Locations | Açaí Bowls | Vitality Bowls"
        HP.getmainlogo().click()

        HP.getbutton_catering().click()
        title = self.driver.title
        assert title == "Catering - Share Fresh Foods With Style! | Açaí Bowls | Vitality Bowls"
        HP.getmainlogo().click()

        HP.getbutton_loyalty_program().click()
        title = self.driver.title
        assert title == "Loyalty Program - Eat Healthy and Earn Points | Açaí Bowls | Vitality Bowls"
        HP.getmainlogo().click()

        HP.getbutton_gift_cards().click()
        title = self.driver.title
        assert title == "Gift Cards | Açaí Bowls | Vitality Bowls"
        HP.getmainlogo().click()

        HP.getbutton_about().click()
        title = self.driver.title
        assert title == "About Vitality Bowls | Açaí Bowls | Vitality Bowls"
        HP.getmainlogo().click()

        HP.getbutton_franchise().click()
        title = self.driver.title
        assert title == "WHO WE ARE | Vitality Bowls"
        self.driver.back()

        HP.getbutton_order_now().click()
        title = self.driver.title
        assert title == "Vitality Bowls"
        self.driver.back()
        #












