class LoginPage:

    textbox_username_id = "Email"
    textbox_password_id = "Password"
    v_rememberMe_id = "RememberMe"
    logIn_button_xpath = "//button[contains(text(),'Log in')]"
    logOut_button_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLoginBtn(self):
        self.driver.find_element_by_xpath(self.logIn_button_xpath).click()

    def click_v_rem_me_btn(self):
        self.driver.find_element_by_id(self.v_rememberMe_id).click()

    def click_LoginOutBtn(self):
        self.driver.find_element_by_link_text(self.logOut_button_linktext).click()

    def login(self, username, password):
        self.setUserName(username)
        self.setPassword(password)
        self.clickLoginBtn()
