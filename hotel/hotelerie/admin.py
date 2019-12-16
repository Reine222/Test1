from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.


@admin.register(models.Type_pieces)

class Type_piecesAdmin(admin.ModelAdmin):

        # AFFICHAGE DES CHAMPS DU MODEL DANS L'ADMIN #
        
        list_display = ('nom', 'prix', 'date_add', 'date_upd', 'statut', 'view_image',)


        # FILTRAGE DU MODEL DANS L'ADMIN #
        
        list_filter = ('date_add', 'date_upd', 'statut',)


        #  CHAMPS DE RECHERCHE DU MODEL DANS L'ADMIN #
        
        search_field = ('nom')


        # MODIFIER LES SATATUTS DU MODEL DANS L'ADMIN #
        
        actions = ('active', 'desactive') 
        def active(self, queryset, request):
            queryset.update(statut == True)
            self.message_user(request, 'Activer une categorie')
        active.short_description = 'active categorie'

        def desactive(self, queryset, request):
            queryset.update(statut == False)
            self.message_user(request, 'Desactiver une categorie')
        desactive.short_description = 'desactive categorie'


        # ORDONNER DES CHAMPS DU MODEL DANS L'ADMIN #
        
        ordering = ('nom',)


        # CREATION DE PAGINATION( 1 element par page dans cet exemple) DANS L'ADMIN #
        
        list_per_page = 5


        # ORDONNER DES CHAMPS DU MODEL EN FONCTION DE LA DATE DANS L'ADMIN #
        
        date_hierarchy = ('date_add')


        # AFFICHAGE DES CHAMPS DU MODEL COMME DES LIENS DANS L'ADMIN #
        
        list_display_links = ('view_image', 'nom',)

        # AFFICHAGE DE L'IMAGE DANS LE DEATAIL DU MODEL DANS L'ADMIN #
        
        readonly_fields = ['detail_image']


        # FONCTION PERMETTANT D'AFFICHER L'IMAGE DANS LA TABLE ET LE DETAIL DU MODEL #
        def view_image(self, obj):
            return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))

        def detail_image(self, obj):
            return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))




@admin.register(models.Caracteristique)

class CaracteristiqueAdmin(admin.ModelAdmin):

        # AFFICHAGE DES CHAMPS DU MODEL DANS L'ADMIN #
        
        list_display = ('nom', 'date_add', 'date_upd', 'statut', 'view_image',)


        # FILTRAGE DU MODEL DANS L'ADMIN #
        
        list_filter = ('date_add', 'date_upd', 'statut',)


        #  CHAMPS DE RECHERCHE DU MODEL DANS L'ADMIN #
        
        search_field = ('nom')


        # MODIFIER LES SATATUTS DU MODEL DANS L'ADMIN #
        
        actions = ('active', 'desactive') 
        def active(self, queryset, request):
            queryset.update(statut == True)
            self.message_user(request, 'Activer une categorie')
        active.short_description = 'active categorie'

        def desactive(self, queryset, request):
            queryset.update(statut == False)
            self.message_user(request, 'Desactiver une categorie')
        desactive.short_description = 'desactive categorie'


        # ORDONNER DES CHAMPS DU MODEL DANS L'ADMIN #
        
        ordering = ('nom',)


        # CREATION DE PAGINATION( 1 element par page dans cet exemple) DANS L'ADMIN #
        
        list_per_page = 5


        # ORDONNER DES CHAMPS DU MODEL EN FONCTION DE LA DATE DANS L'ADMIN #
        
        date_hierarchy = ('date_add')


        # AFFICHAGE DES CHAMPS DU MODEL COMME DES LIENS DANS L'ADMIN #
        
        list_display_links = ('view_image', 'nom',)

        # AFFICHAGE DE L'IMAGE DANS LE DEATAIL DU MODEL DANS L'ADMIN #
        
        readonly_fields = ['detail_image']


        # FONCTION PERMETTANT D'AFFICHER L'IMAGE DANS LA TABLE ET LE DETAIL DU MODEL #
        def view_image(self, obj):
            return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))

        def detail_image(self, obj):
            return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))



@admin.register(models.Evenement)

class EvenementAdmin(admin.ModelAdmin):

        # AFFICHAGE DES CHAMPS DU MODEL DANS L'ADMIN #
        
        list_display = ('auteur', 'titre', 'date', 'description', 'date_add', 'date_upd', 'statut', 'view_image',)


        # FILTRAGE DU MODEL DANS L'ADMIN #
        
        list_filter = ('date_add', 'date_upd', 'statut',)


        #  CHAMPS DE RECHERCHE DU MODEL DANS L'ADMIN #
        
        search_field = ('titre')


        # MODIFIER LES SATATUTS DU MODEL DANS L'ADMIN #
        
        actions = ('active', 'desactive') 
        def active(self, queryset, request):
            queryset.update(statut == True)
            self.message_user(request, 'Activer une categorie')
        active.short_description = 'active categorie'

        def desactive(self, queryset, request):
            queryset.update(statut == False)
            self.message_user(request, 'Desactiver une categorie')
        desactive.short_description = 'desactive categorie'


        # ORDONNER DES CHAMPS DU MODEL DANS L'ADMIN #
        
        ordering = ('titre',)


        # CREATION DE PAGINATION( 1 element par page dans cet exemple) DANS L'ADMIN #
        
        list_per_page = 5


        # ORDONNER DES CHAMPS DU MODEL EN FONCTION DE LA DATE DANS L'ADMIN #
        
        date_hierarchy = ('date')


        # AFFICHAGE DES CHAMPS DU MODEL COMME DES LIENS DANS L'ADMIN #
        
        list_display_links = ('view_image', 'titre',)

        # AFFICHAGE DE L'IMAGE DANS LE DEATAIL DU MODEL DANS L'ADMIN #
        
        readonly_fields = ['detail_image']


        # FONCTION PERMETTANT D'AFFICHER L'IMAGE DANS LA TABLE ET LE DETAIL DU MODEL #
        def view_image(self, obj):
            return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))

        def detail_image(self, obj):
            return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))
