from django.forms import ModelForm
from .models import Produit
from .models import Emballage
from .models import Fournisseur
from .models import Commande
from django.forms import forms
class ProduitForm(ModelForm):
    class Meta:
        model=Produit
        fields= "__all__"

        #fields=['libelle','description']
class CommandeForm(ModelForm):
    class Meta:
        model=Commande
        fields= "__all__"



'''class FrsForm(forms.Form):
    nom=forms.CharField(max_length=30)
    adr=forms.CharField(widget=forms.Textarea)'''
'''class NouveauContactForm(forms.Form):
    nom=forms.CharField()
    adresse=forms.CharField(widget=forms.Textarea)
    photo=forms.ImageField()'''
