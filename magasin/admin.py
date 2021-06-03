from django.contrib import admin
from django.db import models
from .models import Produit
from .models import Emballage
from .models import Fournisseur
from .models import ProduitNC
from .models import Commande
# Register your models here.
admin.site.register(Produit)
admin.site.register(Emballage)
admin.site.register(Fournisseur)
admin.site.register(ProduitNC)
admin.site.register(Commande)

