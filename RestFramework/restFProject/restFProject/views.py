
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rfapp.serializers import StudentSerializer
from rfapp.models import Students

class TesView(APIView):

    permission_classes=(IsAuthenticated, )

    def get(self, request, *args, **kargs):
        qs = Students.objects.all()
        student1 = qs.first()
        serializer = StudentSerializer(student1)
        return Response(serializer.data)
    
    def post(self, request, *args, **kargs):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
