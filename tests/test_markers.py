from playwright.sync_api import sync_playwright
import pytest

@pytest.mark.smoke
def test_some_case():
    ...

@pytest.mark.regression
def test_regression_case():
    ...


@pytest.mark.regression
class TestSuite:

    def test_some_case(self):
        ...

    def test_regression_case(self):
        ...


@pytest.mark.registration
def test_user_registration():
    pass

@pytest.mark.smoke
def test_user_login():
    pass

@pytest.mark.registration
@pytest.mark.regression
def test_password_reset():
    pass