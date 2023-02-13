from selene.support.shared import browser
import pytest


@pytest.fixture
def open_browser_for_desktop():
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    yield
    browser.quit()


@pytest.fixture
def open_browser_for_mobile():
    browser.config.window_width = 300
    browser.config.window_height = 150
    yield
    browser.quit()