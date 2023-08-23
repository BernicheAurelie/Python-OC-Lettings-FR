import time
from selenium.webdriver.common.keys import (
    Keys,
)
from selenium.webdriver.common.by import (
    By,
)
from selenium.webdriver.support.ui import (
    Select,
)
from tests.functionals.test_setup import (
    TestSetUp,
)


class TestProfile(TestSetUp):
    def test_get_lettings(self):
        self.browser.get("http://127.0.0.1:8000/lettings/")
        title = self.browser.find_element(By.TAG_NAME, "h1")
        assert "Lettings" in title.text

    def test_get_a_letting(self):
        self.browser.get("http://127.0.0.1:8000/lettings/")
        letting_link_button = self.browser.find_element(
            By.LINK_TEXT,
            "Joshua Tree Green Haus /w Hot Tub",
        )
        letting_link_button.click()
        title = self.browser.find_element(By.TAG_NAME, "h1")
        assert "Joshua Tree Green Haus /w Hot Tub" in title.text
        street = self.browser.find_element(By.TAG_NAME, "p")
        assert "7217 Bedford Street" in street.text
        state = self.browser.find_elements(By.TAG_NAME, "p")[1]
        assert "Brunswick, GA 31525" in state.text
        country = self.browser.find_elements(By.TAG_NAME, "p")[2]
        assert "USA" in country.text

    def test_back_link(self):
        self.browser.get("http://127.0.0.1:8000/lettings/1/")
        back_button = self.browser.find_element(By.LINK_TEXT, "Back")
        back_button.click()
        title = self.browser.find_element(By.TAG_NAME, "h1")
        assert "Lettings" in title.text

    def test_home_link(self):
        self.browser.get("http://127.0.0.1:8000/lettings/1/")
        home_button = self.browser.find_element(By.LINK_TEXT, "Home")
        home_button.click()
        title = self.browser.find_element(By.TAG_NAME, "h1")
        assert "Welcome to Holiday Homes" in title.text
