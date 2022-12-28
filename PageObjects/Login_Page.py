# Page Object Class for Login page

class login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//input[@class='button-1 login-button']"
    link_logout_linktext = "Logout"
    
    def __init(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.findElement(By.id(self.textbox_username_id)).clear()
        self.driver.findElement(By.id(self.textbox_username_id)).send_keys(username)

    def setPassword(self,password):
        self.driver.findElement(By.id(self.textbox_password_id)).clear()
        self.driver.findElement(By.id(self.textbox_password_id)).send_keys(password)

    def clickLogin(self):
        self.driver.findElement(By.xpath(self.button_login_xpath)).click()

    def clickLogout(self):
        self.driver.findElement(By.linkText(self.link_logout_linktext)).click()


