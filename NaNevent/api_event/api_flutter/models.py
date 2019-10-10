from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Compagnie(models.Model):
    nom_compagnie = models.CharField(max_length=50)
    addresse = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    class Meta:
        """Meta definition for Commune."""

        verbose_name = 'Compagnie'
        verbose_name_plural = 'Compagnies'

    def __str__(self):
        """Unicode representation of Commune."""
        return self.nom_compagnie
    
class Commune(models.Model):
    """Model definition for Commune."""
    nom_commune = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Commune."""

        verbose_name = 'Commune'
        verbose_name_plural = 'Communes'

    def __str__(self):
        """Unicode representation of Commune."""
        return self.nom_commune
    
class Categorie_event(models.Model):
    """Model definition for Categorie_event."""
    nom = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Categorie_event."""

        verbose_name = 'Categorie_event'
        verbose_name_plural = 'Categorie_events'

    def __str__(self):
        """Unicode representation of Categorie_event."""
        return self.nom


class Events(models.Model):
    """Model definition for Events."""
    nom_event = models.CharField(max_length=50)
    date_debut = models.DateField()
    date_fin = models.DateField()
    description = models.TextField()
    lieu = models.CharField(max_length=50)
    id_categorie = models.ForeignKey(Categorie_event, on_delete=models.CASCADE, related_name='categorie_evenement')
    id_commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='commune_evenements')
    id_compagnie = models.ForeignKey(Compagnie, on_delete=models.CASCADE, related_name='compagnie_evenements')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    

    class Meta:
        """Meta definition for Events."""

        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        """Unicode representation of Events."""
        return self.nom_event
    

class ImageEvents(models.Model):
    images = models.URLField()
    event = models.ForeignKey(Events,on_delete=models.CASCADE,related_name='image_event')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Utilisateur(models.Model):
    """Model definition for Utilisateur."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='utilisateur')
    contact = models.CharField(max_length=50)
    id_commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='commune_utilisateur',null=True)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    @receiver(post_save, sender=User)
    def create_user_utilisateur(sender, instance, created, **kwargs):
        if created:
            Utilisateur.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_utilisateur(sender, instance, created, **kwargs):
        instance.utilisateur.save()

    class Meta:
        """Meta definition for Utilisateur."""

        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

    def __str__(self):
        """Unicode representation of Utilisateur."""
        return self.user.username

    
class Participant(models.Model):
    """Model definition for Participant."""
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='participant')
    id_event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='participant_evenement')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Participant."""

        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'

    def __str__(self):
        """Unicode representation of Participant."""
        return self.id_utilisateur


