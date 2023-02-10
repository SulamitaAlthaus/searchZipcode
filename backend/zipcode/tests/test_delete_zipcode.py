import pytest
from .utils import client, payload


@pytest.mark.django_db
def test_delete_zipcode():
    client.post('/cep', payload)
    response = client.delete('/cep/1')
    assert response.status_code == 204


@pytest.mark.django_db
def test_delete_zipcode_no_exist():
    response = client.delete('/cep/4')
    assert response.status_code == 404
    assert response.data["detail"] == "CEP não encontrado."
