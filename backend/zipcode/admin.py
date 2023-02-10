from django.contrib import admin

from .models import ZipCode


class ZipCodeAdmin(admin.ModelAdmin):
    list_display = ("cep", "logradouro", "uf", "ddd", "lojacorr")
    model = ZipCode
    search_fields = ["cep"]


admin.site.register(ZipCode, ZipCodeAdmin)
