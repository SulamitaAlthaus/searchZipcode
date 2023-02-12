from django.db import models


class ZipCode(models.Model):
    cep = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=256, null=True, blank=True)
    complemento = models.CharField(max_length=256, null=True, blank=True)
    bairro = models.CharField(max_length=256, null=True, blank=True)
    localidade = models.CharField(max_length=256, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    ibge = models.CharField(max_length=100, null=True, blank=True)
    gia = models.CharField(max_length=100, null=True, blank=True)
    ddd = models.CharField(max_length=2, null=True, blank=True)
    siafi = models.CharField(max_length=256, null=True, blank=True)
    lojacorr = models.BooleanField(default=False)

    def __str__(self):
        return self.cep

    class Meta:
        verbose_name = "CEP"
        verbose_name_plural = "CEPs"
