from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#from .forms import FrsForm
from .models import *
from .models import Produit
from .models import Commande
from .forms import ProduitForm
from .forms import CommandeForm
#from .forms import NouveauContactForm
from django.shortcuts import redirect

'''def index(request):
    if request.method=="POST":
        formulaire=ProduitForm(request.POST)
        if formulaire.is_valid():
            formulaire.save()
            return redirect('/magasin')
    else:
        formulaire=ProduitForm() #créer une formulaire vide
    return render(request,'magasin/mesProduits.html',{'form':formulaire})'''

def vitrine(request):
    list=Produit.objects.all()
    return render(request,'magasin/vitrine.html',{'list':list})

    

def mesCommandes(request):
    sauvegarde=False
    form=CommandeForm(request.POST, request.FILES)
    if form.is_valid():
        cmd=Commande()
        cmd.Duree_garantie=form.cleaned_data["Duree_garantie"]
        cmd.dateCde=form.cleaned_data["dateCde"]
        cmd.totalCde=form.cleaned_data["totalCde"]
        form.save()
        sauvegarde=True
        return redirect('/magasin/shop')
    else:
        form=CommandeForm()
    return render(request,'magasin/commande.html',{'form':form})
# Create your views here.
def index(request):
    sauvegarde=False
    form = ProduitForm(request.POST, request.FILES)
    if form.is_valid():
        frm = Produit()
        frm.libelle = form.cleaned_data["libelle"]
        frm.description = form.cleaned_data["description"]
        frm.prix = form.cleaned_data["prix"]
        frm.types = form.cleaned_data["types"]
        frm.img = form.cleaned_data["img"]
        frm.emballag = form.cleaned_data["emballag"]
        frm.fournisseur = form.cleaned_data["fournisseur"]
        form.save()
        sauvegarde=True
    else:
        form=ProduitForm()
    return render(request,'magasin/mesProduits.html',{'form':form})
def mesProduits(request):
    prod=loader.get_template('magasin/mesProduits.html')
    list=Produit.objects.all()
    return HttpResponse(prod.render({'liste':list}))
'''def index(request):
    if request.method=="POST":
        form=FrsForm(request.POST)
        if form.is_valid():
            nom=form.cleaned_data['nom']
            adr=form.cleaned_data['adr']
            frs=Fournisseur
            frs.nom=nom
            frs.adresse=adr
            form.save()
    else:
        form=FrsForm()
    return render(request,'magasin/testForm.html',{'form':form})'''

def shop(request):
    list=Commande.objects.all()
    return render(request,'magasin/shop.html',{'list':list })

def indexf(request):
    listf = Fournisseur.objects.all()
    return render(request,'magasin/fournisseur.html',{'listf':listf})