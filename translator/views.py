from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from translator.models import Translation
from translator.serializers import TranslationSerializer

# Create your views here.

class FrenchSpanishTranslationViewSet(APIView):

    def get(self, request):
        return Response(data={}, status=None)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)
    
class FrenchEnglishTranslationViewSet(APIView):

    def get(self, request):
        return Response(data={}, status=None)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)

def index(request):
    return render(request, 'index.html', context={})


def contact(request):
    return render(request, 'contact.html', context={})

# afficher toutes les traductions API
class AllTranslation(APIView):   
    def get(self, request):
# sélectionne toutes les traductions aved la méthode all
        data = Translation.objects.all()
# formater les données en JSON avec le serializer
        serializer_data = TranslationSerializer(data, many=True)
# renvoie les données sérialisées,afficher sous forme de réponse JSON
        return Response(serializer_data.data)
