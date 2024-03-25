from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status



class classeslist(APIView):
    def get(self, request):
        classss = classes.objects.all()
        serializer = ClassSerializer(classss, many= True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = ClassSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        
class classesdetail(APIView):
    def get(self, request, class_id):
        obj = classes.objects.get(id = class_id)
        serializer = ClassSerializer(obj)
        return Response(serializer.data)
    
    def put(self, request, class_id):
        obj = classes.objects.get(id = class_id)
        serializer = ClassSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)
    
    def patch(self, request, class_id):
        obj = classes.objects.get(id=class_id)
        serializer = ClassSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, class_id):
        obj = classes.objects.get(id = class_id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
class assignmentlist(APIView):
    def get(self, request):
        assignments = assignment.objects.all()
        serializer = AssignmentSerializer(assignments, many= True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = AssignmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        
class assignmentdetail(APIView):
    def get(self, request, class_id):
        obj = assignment.objects.get(id = class_id)
        serializer = AssignmentSerializer(obj)
        ass_name = serializer.data["class_associated"].title
        return Response(serializer.data)
    
    def put(self, request, class_id):
        obj = assignment.objects.get(id = class_id)
        serializer = AssignmentSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)
    
    def patch(self, request, class_id):
        obj = assignment.objects.get(id=class_id)
        serializer = AssignmentSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, class_id):
        obj = assignment.objects.get(id = class_id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
class questionlist(APIView):
    def get(self, request):
        ques = questions.objects.all()
        serializer = QuestionSerializer(ques, many= True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        
class questiondetail(APIView):
    def get(self, request, class_id):
        obj = questions.objects.get(id = class_id)
        serializer = QuestionSerializer(obj)
        return Response(serializer.data)
    
    def put(self, request, class_id):
        obj = questions.objects.get(id = class_id)
        serializer = QuestionSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)
    
    def patch(self, request, class_id):
        obj = questions.objects.get(id=class_id)
        serializer = QuestionSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, class_id):
        obj = questions.objects.get(id = class_id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        