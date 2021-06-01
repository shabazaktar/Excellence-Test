from django.db import models
from django.db.models import fields
from rest_framework import serializers
from tast_app.models import CandidateData,test_score


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model=CandidateData
        fields='__all__'
class testscore_serializer(serializers.ModelSerializer):
    class Meta:
        model=test_score
        fields='__all__'