from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CompagnieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom_compagnie',
        'addresse',
        'email',
        'contact',
        'password',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'nom_compagnie',
        'status',
        'date_add',
    )


class CommuneAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom_commune', 'status', 'date_add', 'date_upd')
    list_filter = (
        'nom_commune',
        'status',
        'date_add',

    )
    
class ImageAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'images', 'event', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',

    )


class Categorie_eventAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'nom',
        'status',
        'date_add',
        'date_upd',
    )


class EventsAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom_event',
        'date_debut',
        'date_fin',
        'description',
        'lieu',
        'id_categorie',
        'id_commune',
        'id_compagnie',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'date_debut',
        'date_fin',
        'id_categorie',
        'id_commune',
        'id_compagnie',
        'status',
        'date_add',
        'date_upd',
        'id',
        'nom_event',
        'date_debut',
        'date_fin',
        'description',
        'lieu',
        'id_categorie',
        'id_commune',
        'id_compagnie',
        'status',
        'date_add',
        'date_upd',
    )


class UtilisateurAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'contact',
        'id_commune',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'user',
        'id_commune',
        'status',
        'date_add',
        'date_upd',
        'id',
        'user',
        'contact',
        'id_commune',
        'status',
        'date_add',
        'date_upd',
    )


class ParticipantAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'id_utilisateur',
        'id_event',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'id_utilisateur',
        'id_event',
        'status',
        'date_add',
        'date_upd',
        'id',
        'id_utilisateur',
        'id_event',
        'status',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Compagnie, CompagnieAdmin)
_register(models.Commune, CommuneAdmin)
_register(models.Categorie_event, Categorie_eventAdmin)
_register(models.Events, EventsAdmin)
_register(models.Utilisateur, UtilisateurAdmin)
_register(models.Participant, ParticipantAdmin)
_register(models.ImageEvents, ImageAdmin)
