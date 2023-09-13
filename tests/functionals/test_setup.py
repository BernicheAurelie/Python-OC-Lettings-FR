from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class TestSetUp(StaticLiveServerTestCase):
    """
    Class with generals methods
    which will be applied to our functionals tests
    """

    def setUp(self):
        """Define which webriver id used for tests"""
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Chrome("./tests/functionals/chromedriver.exe")

    def tearDown(self):
        """Close webdriver at the end of the tests"""
        self.browser.close()
