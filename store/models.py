from django.db import models

# Create your models here.


class Caract(models.Model):
    station_ski = models.IntegerField("approche à station ski", null=True)
    piscine  = models.BooleanField("disponible", default=True)



class Appart(models.Model):
    app_id = models.BigAutoField(primary_key=True)
    surface = models.IntegerField("surface", null=True)
    prix = models.IntegerField("price", null=True)
    nb_pièces = models.IntegerField("nombre de pièces", null=True)
    caractéristiques = models.ForeignKey(Caract, on_delete=models.CASCADE)


class Program(models.Model):
    programm_id = models.BigAutoField(primary_key=True)
    program_name = models.CharField('Nom du programme', max_length=200, unique = False)
    statu = models.BooleanField("disponible", default=True)
    appartements = models.ForeignKey(Appart, on_delete=models.CASCADE)
