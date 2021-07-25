from selenium.webdriver.support.ui import Select
from nopcommerce.DataModels.UserData import UserData, Gender, CustomerRole, Newsletter, ManagerVendor
import time
import re


class AdminPage:

    # Add new Customer
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkMenuCustomers_item_xpath = "//a[@href='/Admin/Customer/List']"
    # lnkCustomerRoles_xpath = "//a[@href='/Admin/CustomerRole/List']"
    # lnkCustomersOnline_xpath = "//a[@href='/Admin/OnlineCustomer/List']"
    # lnkVendors_xpath = "//a[@href='/Admin/Vendor/List']"
    # lnkActivityLog_xpath = "//a[@href='/Admin/Admin/ActivityLog/ActivityLogs']"
    # lnkActivityTypes_xpath = "//a[@href='/Admin/ActivityLog/ActivityTypes']"
    # lnkGDRPrequests_xpath = "//a[@href='/Admin/Customer/GdprLog']"
    addNewCustomerBtn_xpath = "//a[@href='/Admin/Customer/Create']"
    setEmailTxt_id = "Email"
    setPasswordTxt_id = "Password"
    setFirstName_id = "FirstName"
    setLastName_id = "LastName"
    setGenderMale_id = "Gender_Male"
    setGenderFemale_id = "Gender_Female"
    setDateofBirth_id = "DateOfBirth"   #MM/DD/YYYY
    btnDateOfBirth_dateview_xpath = "//span[@aria-controls='DateOfBirth_dateview']"
    setCompanyName_css = "#Company"
    drpnewsletter_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    drpNewsLetterMy_xpath = "// li[contains(text(), 'Your store name')]"
    drpNewsLetterTest_xpath = "// li[contains(text(), 'Test store 2')]"
    drpManagerOfVendor_id = "VendorId"
    drpAllCustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemGuests_xpath = "//li[contains (text(), 'Guests')]"
    lstitemAdministrators_xpath = "//li[contains (text(), 'Administrators')]"
    lstitemForum_Moderators_xpath = "//li[contains (text(), 'Forum Moderators')]"
    lstitemVendors_xpath = "//li[contains (text(), 'Vendors')]"
    lstitemRegistered_xpath = "//li[contains (text(), 'Registered')]"
    setAdminComment_id = "AdminComment"
    btnSave_xpath = "//button[@name='save']"
    addedSuccessfuliMsg_xpath_text = "//body[1]/div[3]/div[1]/div[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickCustomersItemMenu(self):
        self.driver.find_element_by_xpath(self.lnkMenuCustomers_item_xpath).click()

    def clickAddNew(self):
        self.driver.find_element_by_xpath(self.addNewCustomerBtn_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_id(self.setEmailTxt_id).clear()
        self.driver.find_element_by_id(self.setEmailTxt_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.setPasswordTxt_id).clear()
        self.driver.find_element_by_id(self.setPasswordTxt_id).send_keys(password)

    def setCustomerRoles(self):
        self.driver.find_element_by_xpath(self.drpAllCustomerRoles_xpath).click()
        time.sleep(5)

    def setFirstName(self, firstname):
        self.driver.find_element_by_id(self.setFirstName_id).clear()
        self.driver.find_element_by_id(self.setFirstName_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element_by_id(self.setLastName_id).clear()
        self.driver.find_element_by_id(self.setLastName_id).send_keys(lastname)

    def setGender(self, gender=Gender):
        if gender == Gender.male:
            self.driver.find_element_by_id(self.setGenderMale_id).click()
        elif gender == Gender.female:
            self.driver.find_element_by_id(self.setGenderFemale_id).click()
        else:
            self.driver.find_element_by_id(self.setGenderMale_id).click()

    def setDateOfBirth(self, dateOfBirth):
        self.driver.find_element_by_id(self.setDateofBirth_id).clear()
        self.driver.find_element_by_id(self.setDateofBirth_id).send_keys(dateOfBirth)

    def setCompanyName(self, company):
        self.driver.find_element_by_css_selector(self.setCompanyName_css).clear()
        self.driver.find_element_by_css_selector(self.setCompanyName_css).send_keys(company)

    def setNewsletter(self, newsletter=Newsletter):
        self.driver.find_element_by_xpath(self.drpnewsletter_xpath).click()
        if newsletter == Newsletter.yourStoreName:
            self.list = self.driver.find_element_by_xpath(self.drpNewsLetterMy_xpath)
        else:
            self.list = self.driver.find_element_by_xpath(self.drpNewsLetterTest_xpath)
        self.driver.execute_script("arguments[0].click();", self.list)

    def setCustomerRoles(self, role=CustomerRole):
        self.driver.find_element_by_xpath(self.drpAllCustomerRoles_xpath).click()
        if role == CustomerRole.registered:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)

        elif role == CustomerRole.administrators:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
            if self.setManagerofVendor() == ManagerVendor.vendor_1 or ManagerVendor.vendor_2:
                self.setManagerofVendor(ManagerVendor.notaVendor)
        elif role == CustomerRole.guests:
            # Here user can be Registered( or) Guest, only one
            time.sleep(0.2)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        elif role == CustomerRole.registered:
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == CustomerRole.vendors:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        else:
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(0.3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerofVendor(self, vendor=ManagerVendor):
        drp = Select(self.driver.find_element_by_id(self.drpManagerOfVendor_id))
        if vendor == ManagerVendor.notaVendor:
            drp.select_by_visible_text('Not a vendor')
        elif vendor == ManagerVendor.vendor_1:
            drp.select_by_visible_text('Vendor 1')
        elif vendor == ManagerVendor.vendor_2:
            drp.select_by_visible_text('Vendor 2')
        else:
            drp.select_by_visible_text('Not a vendor')

        time.sleep(0.5)

    def setAdminComment(self, comment):
        self.driver.find_element_by_id(self.setAdminComment_id).clear()
        self.driver.find_element_by_id(self.setAdminComment_id).send_keys(comment)

    def clickButtonSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()

    def actualMsg(self):
        m = self.driver.find_element_by_xpath(self.addedSuccessfuliMsg_xpath_text).text
        m = re.sub(r'[^ \w]', '', m)
        msg = m.lstrip()
        return msg

    def addNewUser(self, userdata=UserData):
        self.setFirstName(userdata.firstName)
        self.setLastName(userdata.secondName)
        self.setEmail(userdata.email)
        self.setGender(userdata.gender)
        self.setDateOfBirth(userdata.dateofBirth)
        self.setPassword(userdata.password)
        self.setAdminComment(userdata.adminComment)
        self.setManagerofVendor(userdata.managerofVendor)
        self.setNewsletter(userdata.newsletter)
        self.setCompanyName(userdata.companyName)
        self.setCustomerRoles(userdata.customerRole)

    def clickToAddNew(self):
        self.clickCustomerMenu()
        self.clickCustomersItemMenu()
        self.clickAddNew()











