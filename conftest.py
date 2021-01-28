from fixture.application import Application
from fixture.db import DbFixture
import pytest
from json import load
from jsonpickle import decode
from os.path import abspath, dirname, join
from importlib import import_module

fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture

    browser = request.config.getoption("--browser")
    # base_url = request.config.getoption("--baseUrl")

    # web block
    web_config = load_config(request.config.getoption("--target"))["web"]
    if (fixture is None) or (not fixture.is_valid):
        fixture = Application(browser=browser, base_url=web_config["BaseUrl"])
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture

@pytest.fixture(scope = "session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)

@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[repr(x) for x in testdata]) #str
        elif fixture.startswith("json_"):
            testdata = load_from_json_file(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[repr(x) for x in testdata]) #str

def load_from_module(module):
    return import_module(f'data.{module}').debug_data

def load_from_json_file(file):
    path_file = join(dirname(abspath(__file__)), f"data/{file}.json")
    with open(path_file) as j_file:
        return decode(j_file.read())

@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    db_fixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])

    def fin():
        db_fixture.destroy()
    request.addfinalizer(fin)
    return db_fixture

def load_config(file):
    global target
    target_file = join(dirname(abspath(__file__)), file)
    if target is None:
        with open(target_file) as config_file:
            target = load(config_file)
    return target
