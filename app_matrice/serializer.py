from rest_framework import serializers
from .models import User, Profil, Field, Competence

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfilSerializer(serializers.ModelSerializer):
    certification = serializers.StringRelatedField(many=True)
    # society = serializers.StringRelatedField(many=True)
    # workstation = serializers.StringRelatedField(many=True)

    class Meta:
        model = Profil
        fields = '__all__'

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['name']

class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = ['name']
