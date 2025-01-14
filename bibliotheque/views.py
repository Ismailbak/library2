from django.shortcuts import render, get_object_or_404
from .models import Livre

def liste_livres(request):
    livres = Livre.objects.all()
    return render(request, 'bibliotheque/liste_livres.html', {'livres': livres})

def detail_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    return render(request, 'bibliotheque/detail_livre.html', {'livre': livre})
