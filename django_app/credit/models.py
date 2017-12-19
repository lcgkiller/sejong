from django.db import models

# Create your models here.

class Credit(models.Model):
    id = models.AutoField(primary_key=True)
    admission_year = models.IntegerField()              # 입학년도
    college = models.CharField(max_length=30)           # 단과대학
    department = models.CharField(max_length=30)        # 학과명

    core_essential = models.IntegerField()              # 중핵필수
    core_essential_selection = models.IntegerField()    # 중핵필수선택
    major_basic = models.IntegerField()                 # 전공기초교양
    sum_of_major = models.IntegerField()                # 전공학점 합계

    major_required = models.IntegerField()              # 전공필수
    major_select = models.IntegerField()                # 전공선택
    sum_of_all = models.IntegerField()                  # 졸업학점
