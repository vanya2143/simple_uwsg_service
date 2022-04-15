import pytest
from werkzeug.test import Client

from app.app import Application, routes


# Fixtures
@pytest.fixture
def app_fixture():
    def _app():
        app = Application(routes)
        return app
    return _app


def test_sum_of_two(app_fixture):
    app = app_fixture()
    client = Client(app)
    base_url = '/sum_of_two/'

    response = client.get(base_url)
    assert response.status_code == 200
    assert response.json.get('sum_of_two') == False

    args = '?arr=1&arr=2&arr=3'
    response = client.get(base_url + args)
    assert response.status_code == 200
    assert response.json.get('sum_of_two') == True
