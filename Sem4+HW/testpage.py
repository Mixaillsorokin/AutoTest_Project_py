from baseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
        for locator in locators["xpath"].keys():
            ids[locator] = (By.XPATH, locators["xpath"][locator])
        for locator in locators["css"].keys():
            ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator} ")
            return False
        return True

    def click_btn(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    # Enter text
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="Pass form")

    def enter_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_NAME_FIELD"], word, description="Name form")

    def enter_email(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_EMAIL_FIELD"], word, description="Email form")

    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_FIELD"], word, description="Content form")

    # Alert
    def switch_alert(self):
        logging.info("Switch alert")
        text = self.alert()
        logging.debug(text)
        return text

    # click
    def click_login_button(self):
        self.click_btn(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login btn")

    def click_contact_button(self):
        self.click_btn(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description="Contact btn")

    def click_contact_us_button(self):
        self.click_btn(TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"], description="Contact US btn")
