from rest_framework import serializers
from django.contrib.auth.models import User
from hotelerie.models import *


class Type_piecesSerializer(serializers.ModelSerializer):
        class Meta:
            model = Type_pieces
            fields = '__all__'


class CaracteristiqueSerializer(serializers.ModelSerializer):

        class Meta:
            model = Caracteristique
            fields = '__all__'


class EvenementSerializer(serializers.ModelSerializer):
        class Meta:
            model = Evenement
            fields = '__all__'
            depth = 1