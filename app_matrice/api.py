from rest_framework import viewsets
from .serializer import UserSerializer, ProfilSerializer, FieldSerializer, CompetenceSerializer
from .models import User, Profil, Field, Competence

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ProfilViewSet(viewsets.ModelViewSet):
    serializer_class = ProfilSerializer
    queryset = Profil.objects.all()
    
    
class FieldViewSet(viewsets.ModelViewSet):
    serializer_class = FieldSerializer
    queryset = Field.objects.all()

class CompetenceViewSet(viewsets.ModelViewSet):
    serializer_class = CompetenceSerializer
    queryset = Competence.objects.all()
