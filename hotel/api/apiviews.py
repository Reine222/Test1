from rest_framework import viewsets

from hotelerie.models import *
from .serializers import Type_piecesSerializer, CaracteristiqueSerializer, EvenementSerializer


class Type_piecesViewSet(viewsets.ModelViewSet):
        queryset = Type_pieces.objects.all()
        serializer_class = Type_piecesSerializer
        
class CaracteristiqueViewSet(viewsets.ModelViewSet):
        queryset = Caracteristique.objects.all()
        serializer_class = CaracteristiqueSerializer
        
class EvenementViewSet(viewsets.ModelViewSet):
        queryset = Evenement.objects.all()
        serializer_class = EvenementSerializer