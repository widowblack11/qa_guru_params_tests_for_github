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


@pytest.fixture(params=["desktop", "mobile"])
def given_size(request):
    if request.param == "desktop":
        browser.config.window_height = 1920
        browser.config.window_width = 1080
    elif request.param == "mobile":
        browser.config.window_height = 400
        browser.config.window_width = 200

    return request.param