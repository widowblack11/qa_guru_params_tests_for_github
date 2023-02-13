from selene import be
from selene.support.shared import browser


def test_github_desktop(open_browser_for_desktop):
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()
    assert browser.element('#login').should(be.visible)


def test_github_mobile(open_browser_for_mobile):
    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('[href="/login"]').click()
    assert browser.element('#login').should(be.visible)

