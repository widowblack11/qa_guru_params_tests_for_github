import pytest
from selene.support.shared import browser
from selene import be


@pytest.mark.parametrize("width, height", [pytest.param(1020, 800), pytest.param(1024, 768), pytest.param(900, 500)])
def test_for_signin_only_desktop(width, height):
    if height == 768 or width == 900:
        pytest.skip(reason='Размер бразуера не подходит для мобильной версии')
    browser.config.window_width = width
    browser.config.window_height = height
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()
    assert browser.element('#login').should(be.visible)


@pytest.mark.parametrize("width, height", [pytest.param(1024, 768), pytest.param(340, 232), pytest.param(1920, 1080)])
def test_for_signin_only_mobile(width, height):
    if width == 1024 or height == 1080:
        pytest.skip(reason='Размер бразуера не подходит для десктопной версии')
    browser.config.window_width = width
    browser.config.window_height = height
    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('[href="/login"]').click()
    assert browser.element('#login').should(be.visible)

