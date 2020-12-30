from django.db import models

class NutData(models.Model):
    
    NUTR_CONT3 = models.CharField(max_length=50)
    NUTR_CONT2 = models.CharField(max_length=50)
    NUTR_CONT1 = models.CharField(max_length=50)
    SERVING_SIZE = models.CharField(max_length=50)
    MAKER_NAME = models.CharField(max_length=200)
    NUTR_CONT9 = models.CharField(max_length=50)
    NUTR_CONT8 = models.CharField(max_length=50)
    FOOD_CD = models.CharField(max_length=50)
    NUTR_CONT7 = models.CharField(max_length=50)
    NUTR_CONT6 = models.CharField(max_length=50)
    NUTR_CONT5 = models.CharField(max_length=50)
    NUTR_CONT4 = models.CharField(max_length=50)
    DESC_KOR = models.CharField(max_length=200)
    SAMPLING_MONTH_NAME = models.CharField(max_length=200)
    SUB_REF_NAME = models.CharField(max_length=200)
    SAMPLING_REGION_NAME = models.CharField(max_length=200)
    GROUP_NAME = models.CharField(max_length=200)
    RESEARCH_YEAR = models.CharField(max_length=50)
    SAMPLING_REGION_CD = models.CharField(max_length=50)
    SAMPLING_MONTH_CD = models.CharField(max_length=50)
    NUM = models.IntegerField(primary_key=True)
    SEARCH_SCORE = models.IntegerField(default=0)
    def __str__(self):
        return self.DESC_KOR
class FoodDatas(models.Model):
    
    PRDLST_NM = models.CharField(max_length=50)
    PRDLST_DCNM = models.CharField(max_length=50)
    BSSH_NM = models.CharField(max_length=200)
    PRMS_DT = models.CharField(max_length=50)
    RAWMTRL_NM = models.TextField()
    LCNS_NO = models.CharField(max_length=50)
    PRDLST_REPORT_NO = models.CharField(max_length=50)
    PRDLST_NM_NOSPACE = models.CharField(max_length=200,default='PleaseUpLoad')
    SEARCH_SCORE = models.IntegerField(default=0)
    def __str__(self):
        return self.PRDLST_NM


class KitoStandard(models.Model):
    class Level(models.IntegerChoices):
        VeryGood = 1
        Good = 2

        Bad = 3
        FuckingBad = 4
    RW_NAME = models.CharField(max_length=50)
    RW_LEVEL = models.IntegerField(choices=Level.choices)
    RW_EXPLAIN = models.TextField()
