
from django.http.response import HttpResponse
from .models import Commande, Produit, Fournisseur
from .forms import ComForm, FrsForm, ProduitForm
from django.shortcuts import redirect, render
def index(request):
    
    return render(request,'magasin\index.html')


def AjProduit(request):
    if request.method == "POST" :
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/magasin')
    else :
        form = ProduitForm()
    return render(request,'magasin\majProduits.html',{'form':form})


def list_Produit(request):
    list=Produit.objects.all()
    return render(request,'magasin\Produits.html',{'list':list})

def update_Produit(request):
    form = ProduitForm()
    context = {'form':form}

def AjFornisseur(request):
    if request.method == "POST" :
        form = FrsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/magasin')
    else :
        form = FrsForm() 
    return render(request,'magasin\FormFornisseur.html',{'form':form})
def list_Fournisseur(request):
    list=Fournisseur.objects.all()
    return render(request,'magasin\Fornisseur.html',{'list':list})

def AjCommande(request):
    if request.method == "POST" :
        form = ComForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/magasin')
    else :
        form = ComForm() 
    return render(request,'magasin\AjCommande.html',{'form':form})

def list_Commande(request):
    list=Commande.objects.all()
    return render(request,'magasin\Commande.html',{'list':list})


