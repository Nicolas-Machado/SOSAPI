from endereco.serializers import EnderecoSerializer
from .models import Local
from rest_framework import serializers

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ("tipo", "titulo", "numero", "endereco")

class LocalSerializerRetrieve(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    class Meta:
        model = Local
        fields = ("tipo", "titulo", "numero", "endereco")

    