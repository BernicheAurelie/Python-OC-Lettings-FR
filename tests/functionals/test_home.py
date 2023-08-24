from selenium.webdriver.common.by import By
from tests.functionals.test_setup import TestSetUp


class TestHome(TestSetUp):
    """
    class test inherits from TestSetUp 
    to define tests webdriver and tear down method
    """
    def test_get_home(self):
        """
        Test to check access to chrome window and verify template title
        """
        self.browser.get("http://127.0.0.1:8000/")
        title = self.browser.find_element(By.TAG_NAME, "h1")
        assert "Welcome to Holiday Homes" in title.text

    def test_navbar_profiles_link(self):
        """ test to check link to profiles in navbar """
        self.browser.get("http://127.0.0.1:8000/")
        link_to_profile = self.browser.find_elements(By.TAG_NAME, "a")[1]
        link_to_profile.click()
        title = self.browser.find_element(By.TAG_NAME, "h1")
        assert "Profiles" in title.text

    def test_navbar_lettings_link(self):
        """ test to check link to lettings in navbar """
        self.browser.get("http://127.0.0.1:8000/")
        link_to_profile = self.browser.find_elements(By.TAG_NAME, "a")[2]
        link_to_profile.click()
        title = self.browser.find_element(By.TAG_NAME, "h1")
        assert "Lettings" in title.text

    def test_get_profiles_from_home(self,):
        """ test to check link to profiles in home page """
        self.browser.get("http://127.0.0.1:8000/")
        link_to_profile = self.browser.find_elements(By.TAG_NAME, "a")[3]
        link_to_profile.click()
        title = self.browser.find_element(By.TAG_NAME, "h1")
        assert "Profiles" in title.text

    def test_get_lettings_from_home(self,):
        """ test to check link to lettings in home page """
        self.browser.get("http://127.0.0.1:8000/")
        link_to_profile = self.browser.find_elements(By.TAG_NAME, "a")[4]
        link_to_profile.click()
        title = self.browser.find_element(By.TAG_NAME, "h1")
        assert "Lettings" in title.text

    def test_get_wrong_url(self):
        """ test to check custom error 404 page is returned with bad url """
        self.browser.get("http://127.0.0.1:8000/WrongUrl/")
        title = self.browser.find_element(By.TAG_NAME, "h1")
        assert "An error 404 occures" in title.text
        