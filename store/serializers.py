from rest_framework import serializers
from .models import Appart, Program, Caract

class Apparterializer(serializers.ModelSerializer):
    class Meta:
        model = Appart
        fields = '__all__'



class Programmerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'



class Caractrializer(serializers.ModelSerializer):
    class Meta:
        model = Caract
        fields = '__all__'