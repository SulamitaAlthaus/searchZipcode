import pytest
from .utils import client, payload


@pytest.mark.django_db
def test_create_zipcode():
    response = client.post('/cep', payload)
    data = response.data
    assert data['ibge'] == payload['ibge']


@pytest.mark.django_db
def test_create_zipcode_with_uf_lowercase():
    payload['uf'] = 'sc'
    response = client.post('/cep', payload)
    data = response.data
    assert data['uf'] == 'sc'
    assert data['lojacorr'] == True
