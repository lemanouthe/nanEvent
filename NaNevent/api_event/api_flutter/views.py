from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from django.contrib.auth.models import User
from .models import Compagnie,Commune,Events,Utilisateur,Participant,Categorie_event,ImageEvents
from .serializer import CommuneSerializer,CompagnieSerializer,EventSerializer,UtilisateurSerializer,ParticipantSerializer,CategorieSerializer,ImageSerializer
from rest_framework.response import Response

from rest_framework_api_key.permissions import HasAPIKey


# Create your views here.

### dynamic field
class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])
    
    
class CompagnieViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)

    serializer_class = CompagnieSerializer
    queryset = Compagnie.objects.filter(status=True)
    # permission_classes = [HasAPIKey]
    
class CommuneViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    serializer_class = CommuneSerializer
    queryset = Commune.objects.filter(status=True)
    # permission_classes = [HasAPIKey ]
    
class ImageViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    serializer_class = ImageSerializer
    queryset = ImageEvents.objects.filter(status=True)
    # permission_classes = [HasAPIKey ]
    
class EventViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)

    serializer_class = EventSerializer
    queryset = Events.objects.filter(status=True)
    # permission_classes = [HasAPIKey ]
    
class UtilisateurViewset(viewsets.ViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    def list(self, request):
        query_set = Utilisateur.objects.filter(status=True)
        serializer =  self.serializer_class(query_set,many=True)
        return Response(serializer.data)
    def create(self, request):
        print('============',request.POST,'=======================')
        username = request.POST.get('utilisateur.first_name')+' '+request.POST.get('utilisateur.last_name')
        first_name=request.POST.get('utilisateur.first_name')
        last_name=request.POST.get('utilisateur.last_name')
        email=request.POST.get('utilisateur.email')
        password=request.POST.get('utilisateur.password')
        commune = Commune.objects.get(pk=request.POST.get('id_commune'))
        print('===============',commune)
        user = User(username =username, first_name = first_name, last_name = last_name, email = email)
        user.save()
        user.utilisateur.contact = request.POST.get('contact')
        user.utilisateur.id_commune=commune
        user.save()    
        user.password = password
        user.set_password(user.password)
        user.save()
        query_set = Utilisateur.objects.filter(status=True)
        serializer =  self.serializer_class(query_set,many=True)
        return Response(serializer.data)

    def filter(self,queryset):
        for backends in list(self.filter_backends):
            queryset=backends().filter_queryset(self.request,queryset,self)
        return queryset
    
class ParticipantViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)

    serializer_class = ParticipantSerializer
    queryset = Participant.objects.filter(status=True)
    # permission_classes = [HasAPIKey]
    
class CategorieViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)

    serializer_class = CategorieSerializer
    queryset = Categorie_event.objects.filter(status=True)
    # permission_classes = [HasAPIKey]