from django.db import models

# Create your models here.

class Sample(models.Model):
	def __str__(self):
		return str(self.pk)+' '+self.composition
		
	INSTORAGE_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No'),
		)
	LOCATION_CHOICES = (
		('Cabinet 1', 'Cabinet 1'),
		('Cabinet 2', 'Cabinet 2'),
		)	
	
	samplename  = models.CharField("Sample Name", max_length=100,blank=True,null=True)	
	composition = models.CharField("composition", max_length=100)
	otherinfo = models.TextField("Other Info", max_length=500,blank=True,null=True)
	numberOfBoxes = models.IntegerField("Number of Boxes")
	numberOfSamples = models.IntegerField("Number of Samples")
	location = models.CharField(
        max_length=9,
        choices=LOCATION_CHOICES,
        default='Cabinet 1'
        )
	owner = models.CharField("Owner", max_length=100)
	Telephone =  models.CharField("telephone", max_length=12)
	picture = models.ImageField(upload_to='uploads')
	origin = models.CharField("Origin", max_length=100,default='Unknown')
	batch =  models.CharField("Batch", max_length=100,default='Unknown')
	beamtime = models.CharField("Beamtime", max_length=100,blank=True,null=True)
	characterisation = models.CharField("Characterisation", max_length=100,blank=True,null=True)
	date_added = models.DateTimeField(auto_now=True)

	instorage = models.CharField(
        max_length=9,
        choices=INSTORAGE_CHOICES,
        default='No'
        )

class SampleCif(models.Model):
		
	sample=models.ForeignKey(Sample,
	on_delete=models.CASCADE,
	blank=True,
	null=True
	)
	ciffiles=models.FileField(
		upload_to='uploads/ciffiles')

class Reports(models.Model):
	samplereport=models.ForeignKey(Sample,
	on_delete=models.CASCADE,
	blank=True,
	null=True
	)
	beamtime = models.CharField("name", max_length=100,blank=True,null=True)
	pdffiles = models.FileField(
		upload_to='uploads/pdffiles')		
