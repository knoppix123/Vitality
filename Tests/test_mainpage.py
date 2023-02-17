
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

    def testmenu(self):
        HP = Mainpage(self.driver)
        HP.getmainlogo()
        time.sleep(2)

        HP.getmainbutton().click()
        title = self.driver.title
        print(title)
        assert title == "Our Menu | Açaí Bowls | Vitality Bowls"


