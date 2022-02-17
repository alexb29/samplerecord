from django.db import models
import string, random
# Create your models here.


def generatecode():
	return "".join([random.choice(string.ascii_lowercase) for count in range(5)])


class Sample(models.Model):
	def __str__(self):
		return str(self.pk)+' '+self.composition


	INSTORAGE_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No'),
		)
	LOCATION_CHOICES = (
		('Cabinet A', 'Cabinet A'),
		('Cabinet B', 'Cabinet B'),
		('Cabinet C', 'Cabinet C'),
		('Cabinet D', 'Cabinet D'),
		('Other','Other')
		)

	samplename  = models.CharField("Sample Name", max_length=100,blank=True,null=True)
	composition = models.CharField("composition", max_length=100)
	otherinfo = models.TextField("Other Info", max_length=500,blank=True,null=True)
	numberOfBoxes = models.IntegerField("Number of Boxes",default=1)
	numberOfSamples = models.IntegerField("Number of Samples",default=1)
	location = models.CharField(
		max_length=9,
		choices=LOCATION_CHOICES,
		default='Cabinet 1')

	Removedby=models.CharField("Removed by", max_length=100,default='N/A')

	owner = models.CharField("Owner", max_length=100)
	Telephone =  models.CharField("telephone", max_length=12)
	picture = models.ImageField(upload_to='uploads', blank=True,null=True)
	origin = models.CharField("Origin", max_length=100,default='Unknown')
	batch =  models.CharField("Batch", max_length=100,default='Unknown')
	#beamtime = models.CharField("Beamtime", max_length=100,blank=True,null=True)
	characterisation = models.CharField("Characterisation", max_length=100,blank=True,null=True)
	date_added = models.DateTimeField(auto_now=True)
	#samplesmell  = models.CharField("Sample Smell", max_length=100,blank=True,null=True)

	instorage = models.CharField(
		max_length=9,
		choices=INSTORAGE_CHOICES,
		default='No'
		)

	randomidentifier = models.CharField(
		"idstring",max_length=5,editable=False ,unique=True,default=generatecode)


class SamplePictures(models.Model):
	picturesofthesample=models.ForeignKey(Sample,
	on_delete=models.CASCADE,
	blank=True,
	null=True
	)
	picturefiles=models.FileField(
		upload_to='uploads/imagefiles')

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
	beamtime = models.CharField("Beam time", max_length=100,blank=True,null=True)
	pdffiles = models.FileField(
		upload_to='uploads/pdffiles',blank=True,null=True)
	urllink  = models.URLField('LogBook available here',max_length=500, null=True, blank=True)

class TransitionTemperatures(models.Model):

	SampleTransitionTemperature=models.ForeignKey(Sample,
	on_delete=models.CASCADE,
	blank=True,
	null=True
	)

	TRANSITION_CHOICES = (
		('first', 'First Order'),
		('second', 'SEcond Order'),
		('unknown','N/A')
		)

	ORDERING_CHOICES = (
		('Antiferromagnetic', 'Antiferromagnetic'),
		('Ferromagnetic', 'Ferromagnetic'),
		('Ferrimagnetic', 'Ferrimagnetic'),
		('Orbital Ordering','Orbital Ordering'),
		('Charge Ordering', 'Charge Ordering'),
		('N/A','N/A'),
		)

	Temperature = models.FloatField('Transition temperature in K')
	TransitionType = models.CharField('Transition Type',
		max_length=30,
		choices=TRANSITION_CHOICES,
		default='N/A')

	OrderingType = models.CharField('Ordering Type',
		max_length=30,
		choices=ORDERING_CHOICES,
		default='N/A')

	PropagationVector = models.CharField('Propagation Vector',
		max_length=20,
		help_text = "[1/2,1/2,1/2]",
		blank=True,
		null=True)
