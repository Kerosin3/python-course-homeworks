from flask import url_for
from pytest import fixture
from web_app.app import app

@fixture
def client():
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client

def test_reset_stocks(client):
    url = url_for('stocks_app.reset')
    response = client.delete(url)
    data = response.json
    assert data == {'ok':True}
