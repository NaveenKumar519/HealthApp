from django import forms

class brainStrokeForm(forms.Form):
	firstname=forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter Firstname'}))
	lastname=forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter Lastname'}))
	gender=forms.ChoiceField(choices=[('Male', 'Male'),('Female', 'Female')])
	age=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter your age'}))
	hypertension=forms.ChoiceField(choices=[('Yes', 'Yes'),('No', 'No')])
	heart_disease=forms.ChoiceField(choices=[('Yes', 'Yes'),('No', 'No')])
	ever_married=forms.ChoiceField(choices=[('Yes', 'Yes'),('No', 'No')])
	work_type=forms.ChoiceField(choices=[('Private', 'Private'),('Self-employed', 'Self-employed'),('Govt_job', 'Govt_job'),('Never_worked', 'Never_worked'),('children', 'children')])
	Residence_type=forms.ChoiceField(choices=[('Rural', 'Rural'),('Urban', 'Urban')])
	avg_glucose_level=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter average glucose level'}))
	bmi=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter your bmi'}))
	smoking_status=forms.ChoiceField(choices=[('formerly smoked', 'formerly smoked'),('never smoked', 'never smoked'),('smokes', 'smokes')])
	
	