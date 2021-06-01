from django.db import models
from django.db.models.fields import related

# Create your models here.

class CandidateData(models.Model):
    # id=models.IntegerField(primary_key=True)
    c_id=models.AutoField(primary_key=True)
    candidate_name=models.CharField(max_length=20)
    candidate_email=models.EmailField(max_length=20)


class test_score(models.Model):
    # id=models.IntegerField(primary_key=True)
    first_round=models.IntegerField()
    c_id=models.ForeignKey(CandidateData,on_delete=models.CASCADE,related_name="jksds")

    second_round=models.IntegerField()
    third_round=models.IntegerField()
    total=models.IntegerField()

