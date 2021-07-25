import HtmlTestRunner
from selenium import webdriver
import random
import string
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from nopcommerce.DataModels.UserData import UserData, Gender, ManagerVendor, Newsletter, CustomerRole
from nopcommerce.PageObjects.AdminPage import AdminPage
from nopcommerce.PageObjects.LoginPage import LoginPage


class TestAdminPage(unittest.TestCase):

    username = "admin@yourstore.com"
    password = "admin"

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://admin-demo.nopcommerce.com/")
        cls.login = LoginPage(cls.driver)
        cls.login.login(cls.username, cls.password)

    def test_01_titleAdminPage(self):
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False

    def test_02_AddNewCustomer(self):
        self.adminPage = AdminPage(self.driver)
        self.adminPage.clickToAddNew()
        addNewUser = UserData()
        addNewUser.email = random_generator() + "@gmail.com"
        addNewUser.password = "shalala"
        addNewUser.firstName = "jaja"
        addNewUser.secondName = "koka"
        addNewUser.gender = Gender.female
        addNewUser.dateofBirth = "10/10/2000"
        addNewUser.adminComment = "My commentSssa...."
        addNewUser.managerofVendor = ManagerVendor.vendor_2
        addNewUser.companyName = "borodaCo"
        addNewUser.newsletter = Newsletter.yourStoreName
        addNewUser.customerRole = CustomerRole.guests
        self.adminPage.addNewUser(addNewUser)
        self.adminPage.clickButtonSave()
        actualMsg = self.adminPage.actualMsg()
        expectedMsg = "The new customer has been added successfully"
        if actualMsg == expectedMsg:
            assert True
        else:
            assert False

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'nopcommerce/Logs'))