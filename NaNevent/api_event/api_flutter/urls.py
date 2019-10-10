from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategorieViewset,CompagnieViewset,EventViewset,ParticipantViewset,UtilisateurViewset,CommuneViewset,ImageViewset

router = DefaultRouter()
router.register(r'categorie', CategorieViewset, basename='categorie')
router.register(r'compagnie', CompagnieViewset, basename='compagnie')
router.register(r'event', EventViewset, basename='event')
router.register(r'participant', ParticipantViewset, basename='participant')
router.register(r'utilisateur', UtilisateurViewset, basename='utilisateur')
router.register(r'commune', CommuneViewset, basename='commune')
router.register(r'image', ImageViewset, basename='image')


urlpatterns = [
    
]
urlpatterns += router.urls