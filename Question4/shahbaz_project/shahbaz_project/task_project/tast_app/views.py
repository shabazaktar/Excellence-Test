import re
from django.http import response
from rest_framework.serializers import Serializer
from tast_app.serializers import CandidateSerializer
from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView
from tast_app.models import CandidateData,test_score
from tast_app.serializers import CandidateSerializer,testscore_serializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class CandidateCreate(CreateAPIView):
    queryset=CandidateData.objects.all()
    serializer_class=CandidateSerializer

class score_create(CreateAPIView):
    queryset=CandidateData.objects.all()
    serializer_class=testscore_serializer

class get_high(APIView):
    def get(self,request):
        qs=CandidateData.objects.all()
        serializer_class=CandidateSerializer(qs,many=True)
        return Response(serializer_class.data)
   
    
     
    

       




