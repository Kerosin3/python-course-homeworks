from flask import url_for
from pytest import fixture
from app import app

# from web_app import app
@fixture
def client():
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client

def test_dull_test(client):
    url = url_for("stocks_app.test")
    response = client.delete(url)
    data = response.json
    print('data content is ', data)
    assert data == {'ok':True}
# def test_reset_stocks(client):
#     url = url_for("stocks_app.reset")
#     # print('url is',url)
#     # print('TYPE OF THIS', type(url))
#     response = client.delete(url)
#     data = response.json
#     print('data content is ', data)
#     assert data == {'ok':True}
#
#
# def test_c_and_d(client):
#     url = url_for("stocks_app.c&d")
#     response = client.delete(url)
#     data = response.json
#     print('data content is ', data)
#     assert data == {'ok': True}
