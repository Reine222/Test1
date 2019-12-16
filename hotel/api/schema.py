import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from hotelerie.models import *


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class TypePiecesNode(DjangoObjectType):
    class Meta:
        model = Type_pieces
        filter_fields = {
            'nom': ['icontains', 'istartswith'],
            'image': [],
            'prix': ['exact', 'icontains', 'istartswith'],
            'date_add': ['exact', 'icontains', 'istartswith'],
            'date_upd': ['exact', 'icontains', 'istartswith'],
            'statut': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class CaracteristiqueNode(DjangoObjectType):
    class Meta:
        model = Caracteristique
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'image': [],
            'date_add': ['exact', 'icontains', 'istartswith'],
            'date_upd': ['exact', 'icontains', 'istartswith'],
            'statut': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )
        
    
class EvenementNode(DjangoObjectType):
    class Meta:
        model = Evenement
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
            'image': [],
            'date': ['exact', 'icontains', 'istartswith'],
            'date_add': ['exact', 'icontains', 'istartswith'],
            'date_upd': ['exact', 'icontains', 'istartswith'],
            'statut': ['exact', 'icontains', 'istartswith'],
            'auteur' : ['exact'],
            
        }
        interfaces = (relay.Node, )
        
class RelayCreateTypeDePiece(graphene.relay.ClientIDMutation):
    type_de_chambre = graphene.Field(TypePiecesNode)
    class input:
        nom = graphene.String()
        prix = graphene.Float()
    def mutate_and_get_payload(root,info,**kwargs):
        image = info.context.FILES.get('image')
        nom = kwargs.get('nom') or None
        prix = kwargs.get('prix') or None
        
        if image is not None and nom is not None and prix is not None:
            type_de_chambre = Type_pieces(image=image, nom=nom, prix=prix)
        else:
            raise Exception('les paramettre sont requis')
        type_chambre.save()
        return RelayCreateTypeDePiece(type_de_chambre=type_de_chambre)
    
class RelayCreateCaracteristique(graphene.relay.ClientIDMutation):
    caracteristique = graphene.Field(CaracteristiqueNode)
    class input:
        nom = graphene.String()
    def mutate_and_get_payload(root,info,**kwargs):
        image = info.context.FILES.get('image')
        nom = kwargs.get('nom') or None
        
        if image is not None and nom is not None:
            caracteristique = Caracteristique(image=image, nom=nom)
        else:
            raise Exception('les paramettre sont requis')
        caracteristique.save()
        return RelayCreateTypeDePiece(caracteristique=caracteristique)
    
class RelayCreateEvenement(graphene.relay.ClientIDMutation):
    evenement = graphene.Field(EvenementNode)
    class input:
        titre = graphene.String()
        date = graphene.types.datetime.DateTime()
        
    def mutate_and_get_payload(root,info,**kwargs):
        image = info.context.FILES.get('image')
        titre = kwargs.get('titre') or None
        date = kwargs.get('date') or None
        user = info.context.user or None
        
        if image is not None and titre is not None and date is not None and user is not None:
            evenement = Evenement(image=image, titre=titre, user=user, date=date)
        else:
            raise Exception('les paramettre sont requis')
        evenement.save()
        return RelayCreateEvenement(evenement=evenement)
    
    
        
        
    
    
class Query(graphene.ObjectType):
    type_pieces = relay.Node.Field(TypePiecesNode)
    all_type_piecess = DjangoFilterConnectionField(Type_piecesNode)

    caracteristique = relay.Node.Field(CaracteristiqueNode)
    all_caracteristiques = DjangoFilterConnectionField(CaracteristiqueNode)
    
    evenement = relay.Node.Field(EvenementNode)
    all_evenements = DjangoFilterConnectionField(EvenementNode)
    
class RelayMutation(graphene.AbstractType):
    relay_create_type_de_pieces = RelayCreateTypeDePiece.Field()
    relay_create_caracteristique = RelayCreateCaracteristique.Field()
    relay_create_evenement = RelayCreateEvenement.Field()