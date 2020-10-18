from django.db import models

"""
example FoodData json from gonggongDataPotal 
{
PRDLST_NM: "FISH OIL 1200MG CAPSULE",
PRDLST_DCNM: "기타가공품",
BSSH_NM: "(주)서흥",
PRMS_DT: "20061227",
RAWMTRL_NM: "정제어유,젤라틴,글리세린,D-소르비톨",
LCNS_NO: "19930415013",
PRDLST_REPORT_NO: "19930415013457"
}
"""
class FoodDatas(models.Model):
    
    PRDLST_NM = models.CharField(max_length=50)
    PRDLST_DCNM = models.CharField(max_length=50)
    BSSH_NM = models.CharField(max_length=50)
    PRMS_DT = models.CharField(max_length=50)
    RAWMTRL_NM = models.TextField()
    LCNS_NO = models.CharField(max_length=50)
    PRDLST_REPORT_NO = models.CharField(max_length=50)
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