from django.urls import path,include
from django.conf.urls import url
from magasin import views
urlpatterns = [
    path("",views.list_Produit),
    path('ajouter_Produit/', views.AjProduit, name='ajouter_Produit'),
    path('list_Produit/', views.list_Produit, name='Produit'),
    path('ajouter_Fournisseur/', views.AjFornisseur, name='ajouter_Fournisseur'),
    path('list_Fournisseur/', views.list_Fournisseur, name='Fournisseur'),
    path('ajouter_Commande/', views.AjCommande, name='ajouter_Commande'),
    path('list_Commande/', views.list_Commande, name='Commande'),  
    path('index/',views.index) ,   
]
