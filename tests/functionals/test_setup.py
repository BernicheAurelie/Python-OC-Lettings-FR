from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class TestSetUp(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Chrome("tests/functionals/chromedriver")

    def tearDown(self):
        self.browser.close()