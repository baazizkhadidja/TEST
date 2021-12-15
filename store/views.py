from django.shortcuts import render
from models import Appart, Program, Caract

# Create your views here.

#Lister tous les appartements qui dont le programme est actif. (filtrer sur les relations) 
def list_appart(request):
    appart_list = Appart.objects.all().filter(Program.statu = True)
    return render(request, 'index.html',  {'appart_list': appart_list})



#Lister tous les appartements qui ont un prix entre 100k et 180k. (utilisation de Q expressions) 
def list_appart1(request):
    appart_list = Appart.objects.all().filter(Appart.prix in [100, 180])
    return render(request, 'index.html',  {'appart_list': appart_list})



#Lister tous les programmes qui ont au moins un appartement qui contient une piscine. (filtrer
#sur les relations)
def list_appart1(request):
    appart_list = Program.objects.all().filter(Program.appartements.picine == True)
    return render(request, 'index.html',  {'appart_list': appart_list})





#Lister les appartements en ordonnant la réponse en fonction du tri est par prix décroissant, surface décroissante
def list_appart1(request):
    appart_list = Appart.objects.all().filter(Appart['prix'].order_by('prix'))
    return render(request, 'index.html',  {'appart_list': appart_list})
