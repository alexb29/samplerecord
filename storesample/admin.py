from django.contrib import admin
from storesample.models import Sample, SampleCif, Reports,TransitionTemperatures,SamplePictures


class SampleCifInLine(admin.StackedInline):
    model = SampleCif
    extra = 1

class ReportInLine(admin.StackedInline):
	model = Reports
	extra = 1
	

class TransitionTemperaturesInLine(admin.StackedInline):
	model = TransitionTemperatures
	extra = 0


class SamplePicturesInLine(admin.StackedInline):
	model = SamplePictures
	extra = 1

class SampleAdmin(admin.ModelAdmin):
	list_display = ['samplename', 'composition', 'owner']

	inlines=[ SamplePicturesInLine,SampleCifInLine, ReportInLine,TransitionTemperaturesInLine]



# Register your models here.
admin.site.register(Sample,SampleAdmin)
admin.site.register(SampleCif)
admin.site.register(Reports)
admin.site.register(SamplePictures)
admin.site.register(TransitionTemperatures)
