from baseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_CONTACT_BTN = (By.CSS_SELECTOR, """li:nth-child(2) > a""")
    LOCATOR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def click_contact_button(self):
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def enter_name(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_NAME_FIELD[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_NAME_FIELD)
        name_field.clear()
        name_field.send_keys(word)

    def enter_email(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_EMAIL_FIELD[1]}")
        email_field = self.find_element(TestSearchLocators.LOCATOR_EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(word)

    def enter_content(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_CONTENT_FIELD[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(word)

    def click_contact_us_button(self):
        # time.sleep(1)
        logging.info('Click button "Contact us"')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def switch_alert(self):
        logging.info("Switch alert")
        text = self.alert()
        logging.info(text)
        return text
