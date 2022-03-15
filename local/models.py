from django.db import models
from tabnanny import verbose
from django_extensions.db.models import TimeStampedModel

from endereco.models import Endereco

class Local(TimeStampedModel):
    tipo = models.CharField(max_length=100, db_column="TIPO")
    titulo = models.CharField(max_length=100, db_column="TITULO")
    numero = models.CharField(max_length=100, db_column="NUMERO")
    endereco = models.OneToOneField(to=Endereco, on_delete=models.DO_NOTHING, db_column="ENDERECO")

    class Meta:
        db_table = "LOCAL"
        verbose_name = "local"
        verbose_name_plural = "locais"