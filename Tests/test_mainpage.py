import pytest
from selenium import webdriver
import time
from Utilities.BaseClass import BaseClass
from Pages.mainpage import Mainpage
from Pages.orderonlinepage import Orderonlinepage
from Pages.giftcardpage import Giftcardpage
import selenium.common.exceptions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from Pages.giftcardpage_leveldown import Giftcardpage2
from Pages.GiftCard_details_page import Giftcarddatailspage


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


class Testorder(BaseClass):

    def testorder(self):
        HP = Mainpage(self.driver)
        OO = Orderonlinepage(self.driver)
        HP.getbutton_order_online().click()
        time.sleep(2)
        title = self.driver.title
        assert title == "Vitality Bowls"
        OO.getsearch_location_field().send_keys("30009")
        time.sleep(2)
        OO.getsearch_location_result().click()
        time.sleep(1)
        OO.getbutton_search().click()
        time.sleep(1)
        OO.getalpharetta_location().click()
        time.sleep(1)
        OO.getselect_pickup().click()
        time.sleep(1)
        OO.getselect_the_love_bowl().click()
        time.sleep(1)
        OO.getbutton_add_to_bag().click()
        time.sleep(1)
        OO.getbutton_open_bag().click()
        time.sleep(3)


class Testgift(BaseClass):

    def testpurschasegift(self):
        HP = Mainpage(self.driver)
        GC = Giftcardpage(self.driver)
        GC2 = Giftcardpage2(self.driver)
        GC3 = Giftcarddatailspage(self.driver)

        HP.getbutton_giftcard_page().click()
        time.sleep(2)
        GC.getbutton_purchase_gift_card().click()
        title = self.driver.title
        assert title == "Vitality Bowls | Gift Cards"
        GC2.getbutton_purchase_gift_card2().click()
        # header = GC3.getpage_header().text
        header = GC3.getpage_header().get_attribute('innerText')
        print(header)
        assert header == "Please Enter the Details for Your Card"
