from tabnanny import verbose
from django.db import models
from django_extensions.db.models import TimeStampedModel

class Endereco(TimeStampedModel):
    logradouro = models.CharField(max_length=100, db_column="LOGRADOURO")
    cep = models.CharField(max_length=9, db_column="CEP")
    bairro = models.CharField(max_length=100, db_column="BAIRRO")
    cidade = models.CharField(max_length=50, db_column="CIDADE")
    uf = models.CharField(max_length=2, db_column="UF")

    class Meta:
        db_table = "ENDERECO"
        verbose_name = "endereco"
        verbose_name_plural = "enderecos"

    def __str__(self) -> str:
        return self.logradouro