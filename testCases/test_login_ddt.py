import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.Login_Page import LoginPage
from utilities import ExcelUtils
import time
class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationUrl()
    path = ".//TestData/TestData.xlsx"

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

    def test_login_ddt(self,setup):
        self.logger.info("***********test_login_ddt************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path,'Sheet1')
        print(self.rows)
        lst_status=[]
        for r in range(2,self.rows+1):
            self.user = ExcelUtils.readData(self.path,"Sheet1",r , 1)
            self.password = ExcelUtils.readData(self.path,"Sheet1", 'r', 2)
            self.exp = ExcelUtils.readData(self.path,"Sheet1", 'r', 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(set.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopcommerce "
            if act_title == exp_title:
                if self.exp == "Pass":
                    assert True
                    self.lp.clicklogout()
                    self.driver.close()
                    self.logger.info("Login test case failed")
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
                    self.lp.logout()
                    self.driver.close()
                    assert False
                    self.logger.error("Login test case failed")
                    lst_status.append("Pass")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    assert True
                    self.lp.clicklogout()
                    self.driver.close()
                    self.logger.info("Login test case failed")
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
                    self.lp.logout()
                    self.driver.close()
                    assert False
                    self.logger.error("Login test case failed")
                    lst_status.append("Pass")
            if "Fail" not in lst_status:
                self.logger.info("Login DDT Test is Pass")
                self.driver.close()
                assert True
            else:
                self.logger.info("Lodin DDT Test is Failed")
                self.driver.close()
                assert False



