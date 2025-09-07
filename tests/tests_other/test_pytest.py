import pytest

SYSTEM_VERSION = '1.3.0'

@pytest.mark.skip(reason="Not working yet")
def test_fuature_dev():
    pass

@pytest.mark.skipif(
    SYSTEM_VERSION == '1.3.0',
    reason="Будет работать только на определенной версии"
)
def test_version_invalid():
    pass


@pytest.mark.skipif(
    SYSTEM_VERSION == '1.2.0'
)
def test_version_invalid1():
    pass

@pytest.mark.xfail(reason="в пайпе не будет падать прогон, но результат будет помечаться как XFAIL")
def test_with_bug():
    assert False

@pytest.mark.xfail(reason = "Прогон будет помечаться как XPASS, можно снимать xfail")
def test_without_bug():
    pass
