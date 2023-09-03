import yaml
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    url = testdata["address"]


class BasePage:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.base_url = url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Cant find element by locator{locator}')

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        return element.value_of_css_property(property)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def alert(self):
        alert = self.driver.switch_to.alert
        return alert.text