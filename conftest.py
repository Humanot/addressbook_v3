from fixture.application import Application
import pytest
from json import load
from os.path import abspath, dirname, join
from importlib import import_module

fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target

    if (fixture is None) or (not fixture.is_valid):
        browser = request.config.getoption("--browser")
        #base_url = request.config.getoption("--baseUrl")
        target_file = join(dirname(abspath(__file__)), request.config.getoption("--target"))
        if target is None:
            with open(target_file) as config_file:
                target = load(config_file)
        fixture = Application(browser=browser, base_url=target["BaseUrl"])
    fixture.session.ensure_login(username=target["username"], password=target["password"])
    return fixture

@pytest.fixture(scope = "session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--target", action="store", default="target.json")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[repr(x) for x in testdata]) #str

def load_from_module(module):
    return import_module(f'data.{module}').debug_data