from .models import ZipCode
from rest_framework.exceptions import NotFound


def get_zipcode_or_raise_404(id):
    try:
        zipcode = ZipCode.objects.get(id=id)
        return zipcode
    except:
        raise NotFound('CEP não encontrado.')


states_lojacorr = [
    "SP",
    "MS",
    "MT",
    "RO",
    "AC",
    "MG",
    "ES",
    "RJ",
    "GO",
    "DF",
    "PR",
    "SC",
    "RS",
    "PE",
    "AL",
    "AM",
    "PA",
    "CE",
    "MA",
    "PB",
    "PE",
    "PI",
    "BA",
    "SE",
    "RN",
    "TO"
]
