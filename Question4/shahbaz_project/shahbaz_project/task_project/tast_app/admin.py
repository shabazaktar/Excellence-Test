from django.contrib import admin
from tast_app.models import CandidateData,test_score

# Register your models here.
class CandidateAdmin(admin.ModelAdmin):
    model=CandidateData
    list_display=['candidate_name','candidate_email']
class TestscoreAdmin(admin.ModelAdmin):
    model=test_score
    list_display=['first_round','second_round','third_round','total']
admin.site.register(CandidateData,CandidateAdmin)
admin.site.register(test_score,TestscoreAdmin)
