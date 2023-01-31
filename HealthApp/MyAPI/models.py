from django.db import models

# Create your models here.
class brain_stroke(models.Model):
	GENDER_CHOICES = (
		('Male', 'Male'),
		('Female', 'Female')
	)
	MARRIED_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No')
	)
	GRADUATED_CHOICES = (
		('Graduate', 'Graduated'),
		('Not_Graduate', 'Not_Graduate')
	)
	HYPERTENSION_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No')
	)
	HEARTDISEASE_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No')
	)
	RESIDENCETYPE_CHOICES = (
		('Urban', 'Urban'),
		('Rural', 'Rural')
	)
	WORKTYPE_CHOICES = (
		('Private', 'Private'),
		('Self-employed', 'Self-employed'),
		('Govt_job', 'Govt_job'),
		('Never_worked', 'Never_worked'),
		('children', 'children')
	)
	SMOKINGSTATUS_CHOICES = (
		('formerly smoked', 'formerly smoked'),
		('never smoked', 'never smoked'),
		('smokes', 'smokes')
	)
	
	firstname=models.CharField(max_length=15)
	lastname=models.CharField(max_length=15)
	gender=models.CharField(max_length=15, choices=GENDER_CHOICES)
	age=models.IntegerField(default=0)
	hypertension=models.CharField(max_length=15, choices=HYPERTENSION_CHOICES)
	heart_disease=models.CharField(max_length=15, choices=HEARTDISEASE_CHOICES)
	ever_married=models.CharField(max_length=15, choices=MARRIED_CHOICES)
	work_type=models.CharField(max_length=15, choices=WORKTYPE_CHOICES)
	Residence_type=models.CharField(max_length=15, choices=RESIDENCETYPE_CHOICES)
	avg_glucose_level=models.IntegerField(default=0)
	bmi=models.IntegerField(default=0)
	smoking_status=models.CharField(max_length=15, choices=SMOKINGSTATUS_CHOICES)
	

	def __str__(self):
		return '{}, {}'.format(self.lastname, self.firstname)