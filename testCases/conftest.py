from selenium import webdriver
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser...")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser...")
    else:
        driver = webdriver.Ie()
        print("Launching Default Internet Explorer...")
    return driver

def pytest_addpotion(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
#-----------------------------------------

#-------Pytest Html Reports-----------#
# It is a hook for adding Enviroment information to html reports
def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Shivaji'

# it is hook for delete/modify Environment info to html reports
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Java_Home", None)
    metadata.pop("Plugins", None)


