import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'firefox', 'webkit'])
def test_windows(os: str, browser: str):
    assert len(os) > 0


@pytest.fixture(params=['chromium', 'firefox', 'webkit'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f'Получен параметр: {browser}')

@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account:str):
        ...
    def test_user_without_operations(self, user: str):
        ...

user = {
    '+813553155151' : 'user with money',
    '+81241414212' : 'user without money',
    '+125135151633': 'user dont registrations'
}

@pytest.mark.parametrize('phone_number', user.keys(), ids= lambda phone_number: f'{phone_number}: {user[phone_number]}')

def test_identifiers(phone_number: str):
    ...