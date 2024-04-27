import time
import pytest

from selenium import webdriver


@pytest.fixture(scope='class', params=['chrome', 'firefox', 'edge'])
def _drivers(request):
    parameter = request.param

    if parameter == 'chrome':
        driver = webdriver.Chrome()
    elif parameter == 'firefox':
        driver = webdriver.Firefox()
    elif parameter == 'edge':
        driver = webdriver.Edge()


    driver.get('https://demowebshop.tricentis.com/')
    time.sleep(2)
    yield driver
    driver.close()

class TestDemoLogin:

    def test_click_login(self, _drivers):
        _drivers.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(1)

    def test_login_email(self, _drivers):
        _drivers.find_element('xpath', '//input[@id="Email"]').send_keys('meghashankar@gmail.com')

    def test_login_pwd(self, _drivers):
        _drivers.find_element('xpath', '//input[@id="Password"]').send_keys('megha@12345')
