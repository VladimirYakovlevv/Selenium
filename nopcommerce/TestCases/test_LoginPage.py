import HtmlTestRunner
from selenium import webdriver
import time
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from nopcommerce.PageObjects.LoginPage import LoginPage


class LoginPageTest(unittest.TestCase):

    username = "admin@yourstore.com"
    password = "admin"

    # @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://admin-demo.nopcommerce.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)

    def test_01_LoginPageTitle(self):
        act_titl = self.driver.title
        act_titl.title()
        if act_titl == "Your store. Login":
            assert True
        else:
            assert False

    def test_03_LoginPageLogIn(self):
        self.login.login(self.username, self.password)
        self.login.click_LoginOutBtn()

    def test_02_LoginPageV(self):
        self.login.click_v_rem_me_btn()
        self.login.login(self.username, self.password)
        self.login.click_LoginOutBtn()

    def test_04_LoginPageLogOut(self):
        self.login.login(self.username, self.password)
        self.login.click_LoginOutBtn()

    # @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'nopcommerce/Logs'))