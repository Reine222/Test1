
from rest_framework.routers import DefaultRouter
from .apiviews import *


router = DefaultRouter()
router.register('type_pieces', Type_piecesViewSet, base_name='type_pieces')
router.register('caracteristique', CaracteristiqueViewSet, base_name='caracteristique')
router.register('evenement', EvenementViewSet, base_name='evenement')


urlpatterns = [
      # ...
]

urlpatterns += router.urls