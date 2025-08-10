from playwright.sync_api import expect, Page
import pytest

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):


        chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_registration = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
        email_registration.fill('user.name@gmail.com')

        username_registration = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
        username_registration.fill('username')

        password_registration = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
        password_registration.fill('password')

        registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard_title).to_be_visible()


