from app import app
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_search_mercadolivre_category(client):
    response = client.get('/search_meli_by_category?category=celulares-telefones')
    assert response.status_code == 200
    assert len(response.json) > 0


def test_search_mercadolivre_keyword(client):
    response = client.get('/search_meli_by_keyword?category=celulares-telefones&keyword=iphone')
    assert response.status_code == 200
    assert len(response.json) > 0


def test_search_buscape_by_category(client):
    response = client.get('/search_buscape_by_category?category=celular')
    assert response.status_code == 200
    assert len(response.json) > 0


def test_search_buscape_keyword(client):
    response = client.get('/search_buscape_by_keyword?category=celular&keyword=iphone')
    assert response.status_code == 200
    assert len(response.json) > 0


def test_search_all(client):
    response = client.get('/search_all_by_category?category=celular&keyword=iphone')
    assert response.status_code == 200
    assert len(response.json) > 0
