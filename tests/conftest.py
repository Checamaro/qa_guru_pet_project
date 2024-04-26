import os
from selene import browser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import test_attachments
from dotenv import load_dotenv

DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.base_url = 'https://planetainstrument.ru/'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.driver = driver

    yield browser

    test_attachments.add_screenshot(browser)
    test_attachments.add_logs(browser)
    test_attachments.add_html(browser)
    test_attachments.add_video(browser)

    browser.quit()
