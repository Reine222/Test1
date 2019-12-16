from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Type_pieces(models.Model):
    image = models.ImageField(upload_to='images')
    nom = models.CharField(max_length=250)
    prix = models.FloatField()
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    statut = models.BooleanField()



class Caracteristique(models.Model):
    image = models.CharField(max_length=250)
    nom = models.CharField(max_length=250)
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    statut = models.BooleanField()


class Evenement(models.Model):
    image = models.ImageField(upload_to='images')
    titre = models.CharField(max_length=250)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=True)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    statut = models.BooleanField()