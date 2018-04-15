from django.db import models

# Create your models here.
class Reg(models.Model):
	First_Name = models.CharField(max_length=200)
	Last_Name = models.CharField(max_length=200)
	GENDER_CHOICES = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Other', 'Other'),
    )
	Gender = models.CharField(max_length=9, choices=GENDER_CHOICES,
                               default="Male")