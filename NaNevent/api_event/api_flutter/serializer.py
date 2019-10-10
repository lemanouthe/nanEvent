from rest_framework import serializers
from .models import Compagnie,Commune,Events,Utilisateur,Participant,Categorie_event,ImageEvents
from django.contrib.auth.models import User

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'
class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ImageEvents
        fields = '__all__'
        # depth = 1
class EventSerializer(serializers.ModelSerializer):
    participant_evenement = ParticipantSerializer(many=True, required=False)
    image_event = ImageSerializer(many=True,required=False)
    class Meta:
        model = Events
        fields = '__all__'
        # depth = 1

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',      
        ]
        # depth = 1
        

class UtilisateurSerializer(serializers.ModelSerializer):
    participant = ParticipantSerializer(many=True, required=False)
    utilisateur = UserSerializer(many=True,required=False)
    class Meta:
        model = Utilisateur
        # fields = ('contact','id_commune','participant','utilisateur')
        fields = '__all__'
        depth = 1


class CategorieSerializer(serializers.ModelSerializer):
    categorie_evenement = EventSerializer(many=True, required=False)
    class Meta:
        model = Categorie_event
        fields = '__all__'
        depth = 1

class CommuneSerializer(serializers.ModelSerializer):
    commune_evenements=EventSerializer(many=True, required=False)
    class Meta:
        model = Commune
        fields = '__all__'
        depth = 2

class CompagnieSerializer(serializers.ModelSerializer):
    compagnie_evenements= EventSerializer(many=True, required=False)
    class Meta:
        model = Compagnie
        fields = '__all__'