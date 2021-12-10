from rest_framework import serializers
from .models import NbaMod, NflMod, NcaaMod

class NbaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NbaMod
        fields = ['match']


class NflSerializer(serializers.ModelSerializer):
    class Meta:
        model = NflMod
        fields = ['match']

class NcaaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NcaaMod
        fields = ['match']
