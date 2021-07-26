from app import app
from web_app.models import test_me_models
from pytest import fixture

@fixture
def client():
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client

def test_test_me_models(client):
    data = test_me_models()
    assert data == True
