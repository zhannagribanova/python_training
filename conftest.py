from fixture.application import Application
import pytest

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_URL = request.config.getoption("--baseURL")
    if fixture is None:
        fixture = Application(browser=browser, base_URL=base_URL)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_URL=base_URL)
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseURL", action="store", default="http://localhost/addressbook/")
