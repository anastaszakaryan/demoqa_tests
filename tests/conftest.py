from selene.support.shared import browser
import pytest

@pytest.fixture(scope='function', autouse=True)
def browser_managment():
        # browser.config.base_url = 'https://demoqa.com' # дефолтный url
        browser.config.browser_name = 'chrome'
        browser.config.hold_browser_open = True

