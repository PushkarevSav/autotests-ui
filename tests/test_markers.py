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


@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        ...
    @pytest.mark.slow
    def test_password_reset(self):
        ...


    def test_logout(self):
        ...