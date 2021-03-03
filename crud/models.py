from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.core.validators import int_list_validator

# Create your models here.
class itemsPost(models.Model):
    STATUS_CHOICES	=	(
        ('metal',	'metal'),
        ('plastic',	'plastic'),
        ('metal & plastic', 'metal & plastic'),
        )
    itemCode = models.IntegerField( unique=True, null=True)
    itemName = models.CharField(max_length=200)
    techSpecs = models.TextField()
    make = models.CharField(max_length=100, choices = STATUS_CHOICES)
    UOM = models.CharField(max_length = 50)
    rate = models.DecimalField(max_digits=100, decimal_places=2)

    class Meta:
        ordering = ('rate',)

    def __str__(self):
        return self.itemName

class saveOrder(models.Model):
    
    code =models.CharField(max_length=200)
    itemCode =  models.IntegerField(  null=True)
    make = models.CharField(max_length=100, default='number')
    unit = models.CharField(max_length=100, null = True)
    quantity = models.FloatField(null = True, default=1)
    rate = models.FloatField( null = True)
    amount = models.FloatField( null = True)
    center = models.CharField(max_length=200, default='center1')

    class Meta:
        ordering = ('code',)

    def __str__(self):
        return self.code

class requestS(models.Model):

    documentName = models.CharField(max_length = 252)
    documentDate = models.DateField(null = True, default = timezone.now )
    itemName =models.CharField(max_length=200)
    make = models.CharField(max_length=100, default='number')
    UOM = models.CharField(max_length=100, null = True)
    quantity = models.FloatField(null = True, default=1)
    rate = models.FloatField( null = True)
    amount = models.FloatField( null = True)
    requiredOn = models.DateField(null=True, default = timezone.now )
    remarks = models.TextField(null=True)

class set(models.Model):
    
    companyName = models.CharField(max_length = 252)
    # arr = ArrayField(models.IntegerField(null=True, blank=True), null=True, blank=True)
    # v1 = models.CharField(validators=[int_list_validator], max_length=100, null=True)
    requestedBy = models.CharField(max_length = 252 , null=True)
    q1 = models.CharField(max_length = 252 , null=False)
    dN = models.CharField(max_length = 252, null=False) 
    dD =  models.DateField(null = False)
    remarks = models.TextField(null=True)

    class Meta:
        ordering = ('dN','dD')

    def __str__(self):
        return self.dN
