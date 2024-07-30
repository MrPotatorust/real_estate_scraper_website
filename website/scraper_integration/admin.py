from django.contrib import admin
from .models import TableInfo, ScrapedData, AnalysedData

# Register your models here.

admin.site.register(TableInfo)
admin.site.register(ScrapedData)
admin.site.register(AnalysedData)