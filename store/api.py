from .models import Appart, Program, Caract
from .serializers import Apparterializer, Programmerializer, Caractrializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse




class ListAppart(generics.ListAPIView):
    queryset = Appart.objects.all()
    serializer_class = Apparterializer


class ListProg(generics.ListAPIView):
    queryset = Program.objects.all()
    serializer_class = Programmerializer


class ListCaract(generics.ListAPIView):
    queryset = Appart.objects.all()
    serializer_class = Caractrializer



@api_view(['POST'])
def appart_add_api(request):
    appart_data = JSONParser().parse(request)
    apparterializer = Apparterializer(data=appart_data)
    if Apparterializer.is_valid():
        Apparterializer.save()
        return JsonResponse(apparterializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(apparterializer.errors, status=status.HTTP_400_BAD_REQUEST)