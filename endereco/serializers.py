from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from endereco.models import Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        #field =() incluir o que vai ser serializado
        exclude = ('modified', 'created') #exclui o que não precisa ser serializado