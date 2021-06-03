from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from . import views
urlpatterns=[
    path('',views.index,name='ajp'),
    path('Commandes',views.mesCommandes,name='Commandes'),
    path('vitrine',views.vitrine,name='vitrine'),
    path('shop',views.shop,name='shop'),
    path('fournisseur',views.indexf,name='fournisseur'),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

