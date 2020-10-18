from django.contrib import admin
from api.models import FoodDatas, KitoStandard

class FoodAdmin(admin.ModelAdmin):
    fields = ['PRDLST_NM', 'PRDLST_DCNM', 'BSSH_NM', 'PRMS_DT', 'RAWMTRL_NM', 'LCNS_NO', 'PRDLST_REPORT_NO' ]

class KitoStandardAdmin(admin.ModelAdmin):
    fields = ['RW_NAME', 'RW_LEVEL', 'RW_EXPLAIN' ]
admin.site.register(FoodDatas, FoodAdmin)
admin.site.register(KitoStandard, KitoStandardAdmin)

