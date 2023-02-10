import pytest
from .utils import client, payload


@pytest.mark.django_db
def test_update_zipcode():
    client.post('/cep', payload)
    payload["logradouro"] = "Teste logradouro"
    response = client.put('/cep/1', payload)
    data = response.data
    assert data['logradouro'] == "Teste logradouro"


@pytest.mark.django_db
def test_update_zipcode_no_exist():
    response = client.delete('/cep/4')
    assert response.status_code == 404
    assert response.data["detail"] == "CEP não encontrado."
