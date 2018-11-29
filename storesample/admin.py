from django.contrib import admin
from storesample.models import Sample, SampleCif, Reports 


class SampleCifInLine(admin.StackedInline):
    model = SampleCif
    extra = 1

class ReportInLine(admin.StackedInline):
	model = Reports
	extra = 1
	

class SampleAdmin(admin.ModelAdmin):  
	
	inlines=[ SampleCifInLine, ReportInLine]
	


# Register your models here.
admin.site.register(Sample,SampleAdmin)
admin.site.register(SampleCif)
admin.site.register(Reports)
