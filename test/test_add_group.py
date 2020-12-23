from model.group import Group
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_new_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Friends", header="Mine", footer="Dear ones"))
    app.logout()

