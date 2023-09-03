import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]


@pytest.fixture(scope='session')
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def x_selector_1():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def x_selector_2():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def btn_selector():
    return "button"


@pytest.fixture()
def result():
    return "401"


@pytest.fixture()
def hello_user():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""


@pytest.fixture()
def btn_create_post():
    return """#create-btn"""


@pytest.fixture()
def enter_title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def enter_descr():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def enter_content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def btn_save_post():
    return "button > span"


@pytest.fixture()
def post_name():
    return """//*[@id="app"]/main/div/div[1]/h1"""
