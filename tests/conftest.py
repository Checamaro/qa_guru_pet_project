import os
from lib2to3.pgen2 import driver

from selene import browser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import test_attachments
from dotenv import load_dotenv

@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser.config.base_url = 'https://planetainstrument.ru/'
    browser.config.window_width = 1900
    browser.config.window_height = 1000
    browser.config.driver = driver

    yield browser

    test_attachments.add_screenshot(browser)
    test_attachments.add_logs(browser)
    test_attachments.add_html(browser)
    test_attachments.add_video(browser)

    browser.quit()