import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] отправляе данные в сервис аналитики")

@pytest.fixture(scope='session') #Запускается один раз в сессию
#@pytest.fixture(scope='package') #Для пакета init
#@pytest.fixture(scope = 'module') # Запущена один раз для файла
def settings():
    print("[SESSION] инициализация настроек автотестов")

@pytest.fixture(scope='class')
def user():
    print("[CLASS] Создаем данные пользователя один раз на тестовый класс")

@pytest.fixture(scope='function')
def browser():
    print("[FUNCTION] ОТКРЫВАЕМ БРАУЗЕР НА КАЖДЫЙ АВТОТЕСТЫ")

class TestUserFlow:
    def test_user_can_login(self,settings, user, browser):
        ...
    def test_user_can_logout(self,settings, user, browser):
        ...

class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        pass