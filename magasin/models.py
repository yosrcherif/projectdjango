from django.db import models
from datetime import date
# Create your models here.
class Produit(models.Model):
    libelle=models.CharField(max_length=100)
    description=models.TextField(default='non definie')
    prix=models.DecimalField(max_digits=10,decimal_places=3,null=True)
    TYPE_CHOICES=[
        ('em','Emballé'),
        ('fr','Frais'),
        ('cs','Conserve')
    ]
    types=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img=models.ImageField(blank=True,upload_to="media/")
    emballag=models.OneToOneField('Emballage', on_delete=models.CASCADE,null=True)
    fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return 'libellé:{} , description:{} , prix:{} , type:{} , image:{}'.format(self.libelle,self.description,self.prix,self.types,self.img)


class Emballage(models.Model):
    matiere=models.CharField(max_length=100)
    COUL_CHOICES=[
        ('bl','blanc'),
        ('rg','rouge'),
        ('ble','bleue'),
        ('vr','vert'),
        ('multi','multicolore'),
        ('trans','transparent')
    ]
    couleur=models.CharField(max_length=10,choices=COUL_CHOICES,default='Transparent')
    def __str__(self):
        return 'Matiere:{} , Couleur:{}'.format(self.matiere,self.couleur)


class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField(default='null')
    email=models.EmailField(default='null')
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return 'Nom:{} , Adresse:{} , Email:{} , Telephone:{}'.format(self.nom,self.adresse,self.email,self.telephone)


class ProduitNC(Produit,models.Model):
    Duree_garantie=models.CharField(max_length=100)
    def __str__(self):
        return 'libellé:{} , description:{} , prix:{} , type:{} , image:{} , Duree de garantie:{}'.format(self.libelle,
        self.description,self.prix,self.types,self.img,self.Duree_garantie)


class Commande(models.Model):
    Duree_garantie=models.CharField(max_length=100)
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField('Produit')
    def __str__(self):
        return 'Duree garantie:{} , date commande:{} , total commande:{} '.format(self.Duree_garantie,
        self.dateCde,self.totalCde)


