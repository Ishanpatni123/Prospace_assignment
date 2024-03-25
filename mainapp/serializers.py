from rest_framework import serializers
from .models import *


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = classes
        fields = '__all__'
     
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = assignment
        fields = '__all__'   
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = questions
        fields = '__all__'   