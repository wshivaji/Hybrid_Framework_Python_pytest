import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.Login_Page import LoginPage

class Test_001_Login:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserMail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homepageTitle(self):
        self.logger.info("************test_homepageTitle*****************")
        self.logger.info("**********verifying page load************")

        self.driver = setup
        self.driver = get(self.baseURL)

        if act_title == "Your Store. Login":
            assert True
            self.driver.close()
            logger.info("Login test case passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            self.driver.close()
            self.logger.error("test case failed")
            assert False

    def test_login(self):
        self.logger.info("***********test_login************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(set.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close
        if act_title == "Dashboard / nopcommerce ":
            assert True
            self.driver.close()
            self.logger.info("Login test case failed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False
            self.logger.error("Login test case failed")


