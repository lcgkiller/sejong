from django.db import models
# Create your models here.

class Credit(models.Model):
    id = models.AutoField(primary_key=True)
    admission_year = models.IntegerField()              # 입학년도
    college = models.CharField(max_length=30)           # 단과대학
    department = models.CharField(max_length=30)        # 학과명

    core_essential = models.IntegerField()              # 중핵필수 (EX : English Composition, 쓰기와 말하기, 사회와 가치, 신입생 세미나 등)
    core_essential_selection = models.IntegerField()    # 중핵필수선택 (EX : 정보사회의사이버윤리, 과학사, 세종리더십 등)
    major_basic = models.IntegerField()                 # 전공기초교양 (EX : 경영수학, 경영통계학, 공업수학, 고등미적분학 등)
    sum_of_major = models.IntegerField()                # 전공학점 합계

    major_required = models.IntegerField()              # 전공필수
    major_select = models.IntegerField()                # 전공선택
    sum_of_all = models.IntegerField()                  # 졸업학점

    def __str__(self):
        return str(self.core_essential, self.core_essential_selection, self.major_required, self.major_select, self.sum_of_all)