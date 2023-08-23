import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from tests.functionals.test_setup import TestSetUp


class TestProfile(TestSetUp):
    def test_get_profiles(self):
        self.browser.get("http://127.0.0.1:8000/profiles/")
        title = self.browser.find_element(By.TAG_NAME, 'h1')
        assert "Profiles" in title.text

    def test_get_a_profile(self):
        self.browser.get("http://127.0.0.1:8000/profiles/")
        profile_link_button = self.browser.find_element(By.LINK_TEXT, "HeadlinesGazer")
        profile_link_button.click()
        title = self.browser.find_element(By.TAG_NAME, 'h1')
        assert "HeadlinesGazer" in title.text
        first_name = self.browser.find_element(By.TAG_NAME, 'p')
        assert 'Jamie' in first_name.text
        last_name = self.browser.find_elements(By.TAG_NAME, 'p')[1]
        assert 'Lal' in last_name.text
        email = self.browser.find_elements(By.TAG_NAME, 'p')[2]
        assert 'jssssss33@acee9.live' in email.text
        favorite_city = self.browser.find_elements(By.TAG_NAME, 'p')[3]
        assert 'Buenos Aires' in favorite_city.text

    def test_back_link(self):
        self.browser.get("http://127.0.0.1:8000/profiles/HeadlinesGazer/")
        back_button = self.browser.find_element(By.LINK_TEXT, "Back")
        back_button.click()
        title = self.browser.find_element(By.TAG_NAME, 'h1')
        assert 'Profiles' in title.text
    
    def test_home_link(self):
        self.browser.get("http://127.0.0.1:8000/profiles/HeadlinesGazer/")
        home_button = self.browser.find_element(By.LINK_TEXT, "Home")
        home_button.click()
        title = self.browser.find_element(By.TAG_NAME, 'h1')
        assert 'Welcome to Holiday Homes' in title.text