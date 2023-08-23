import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from tests.functionals.test_setup import TestSetUp


class TestHome(TestSetUp):
    def test_get_home(self):
        self.browser.get("http://127.0.0.1:8000/")
        title = self.browser.find_element(By.TAG_NAME, 'h1')
        assert "Welcome to Holiday Homes" in title.text

    def test_navbar_profiles_link(self):
        self.browser.get("http://127.0.0.1:8000/")
        link_to_profile = self.browser.find_elements(By.TAG_NAME, 'a')[1]
        link_to_profile.click()
        title = self.browser.find_element(By.TAG_NAME, 'h1')
        assert "Profiles" in title.text

    def test_navbar_lettings_link(self):
        self.browser.get("http://127.0.0.1:8000/")
        link_to_profile = self.browser.find_elements(By.TAG_NAME, 'a')[2]
        link_to_profile.click()
        title = self.browser.find_element(By.TAG_NAME, 'h1')
        assert "Lettings" in title.text

    def test_get_profiles_from_home(self):
        self.browser.get("http://127.0.0.1:8000/")
        link_to_profile = self.browser.find_elements(By.TAG_NAME, 'a')[3]
        link_to_profile.click()
        title = self.browser.find_element(By.TAG_NAME, 'h1')
        assert "Profiles" in title.text

    def test_get_lettings_from_home(self):
        self.browser.get("http://127.0.0.1:8000/")
        link_to_profile = self.browser.find_elements(By.TAG_NAME, 'a')[4]
        link_to_profile.click()
        title = self.browser.find_element(By.TAG_NAME, 'h1')
        assert "Lettings" in title.text

    