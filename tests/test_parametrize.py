import pytest
from selene import be
from selene.support.shared import browser


@pytest.mark.parametrize("given_size", ['desktop'], indirect=True)
def test_login_desktop_indirect(given_size):
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()

    assert browser.element('#login').should(be.visible)


@pytest.mark.parametrize("given_size", ["mobile"], indirect=True)
def test_login_mobile_indirect(given_size):
    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('[href="/login"]').click()

    assert browser.element('#login').should(be.visible)

