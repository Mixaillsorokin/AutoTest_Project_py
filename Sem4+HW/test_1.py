import yaml
from testpage import OperationsHelper
import logging
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    log = testdata["login"]
    pas = testdata["passwd"]


def test_step1(browser):
    logging.info('Test started')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(log)
    testpage.enter_pass(pas)
    testpage.click_login_button()
    testpage.click_contact_button()
    time.sleep(3)
    testpage.enter_name('Sorokin Mikhail')
    testpage.enter_email('mixa@mail.ru')
    testpage.enter_content('Hello,people!!!')
    time.sleep(3)
    testpage.click_contact_us_button()
    time.sleep(3)
    assert testpage.alert() == 'Form successfully submitted'
