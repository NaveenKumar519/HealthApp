from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from . forms import brainStrokeForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from . models import brain_stroke
from . serializers import brainStrokeSerializers
import pickle
from keras import backend as K
import joblib
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import pandas as pd
from collections import defaultdict, Counter


class brainStrokeView(viewsets.ModelViewSet):
	queryset = brain_stroke.objects.all()
	serializer_class = brainStrokeSerializers
# ohe_col=joblib.load("/Users/sahityasehgal/Documents/Coding/DjangoApiTutorial/DjangoAPI/MyAPI/allcol.pkl")
def ohevalue(df):
	ohe_col=joblib.load("D:/MajorProject/HealthApp/MyAPI/brain_stroke2.pkl")
	return ohe_col
	cat_columns=['gender','hypertension','heart_disease','ever_married','work_type', 'residence_type', 'smoking_status']
	df_processed = pd.get_dummies(df, columns=cat_columns)
	# df_processed = pd.get_dummies(df, drop_first= True)
	# return df
	# return df_processed
	
	# newdict={}
	# for i in ohe_col:
	# 	if i in df_processed.columns:
	# 		newdict[i]=df_processed[i].values
	# 	else:
	# 		newdict[i]=0
	# newdf=pd.DataFrame(newdict)
	# return newdf

def approvereject(unit):
	try:
		mdl=joblib.load("C://Users/sahityasehgal/Documents/Coding/DjangoApiTutorial/DjangoAPI/MyAPI/loan_model.pkl")
		scalers=joblib.load("/Users/sahityasehgal/Documents/Coding/DjangoApiTutorial/DjangoAPI/MyAPI/scalers.pkl")
		X=scalers.transform(unit)
		y_pred=mdl.predict(X)
		y_pred=(y_pred>0.58)
		newdf=pd.DataFrame(y_pred, columns=['Status'])
		newdf=newdf.replace({True:'Approved', False:'Rejected'})
		K.clear_session()
		return (newdf.values[0][0],X[0])
	except ValueError as e:
		return (e.args[0])

def cxcontact(request):
	if request.method=='POST':
		form=brainStrokeForm(request.POST)
		if form.is_valid():
				firstname = form.cleaned_data['firstname']
				lastname = form.cleaned_data['lastname']
				gender = form.cleaned_data['gender']
				age = form.cleaned_data['age']
				hypertension = form.cleaned_data['hypertension']
				heart_disease = form.cleaned_data['heart_disease']
				ever_married = form.cleaned_data['ever_married']
				work_type = form.cleaned_data['work_type']
				Residence_type = form.cleaned_data['Residence_type']
				avg_glucose_level = form.cleaned_data['avg_glucose_level']
				bmi = form.cleaned_data['bmi']
				smoking_status = form.cleaned_data['smoking_status']
				
				myDict = (request.POST).dict()
				genderMale = 0
				ever_married_Yes = 0
				hypertension_1 = 0
				heart_disease_1 = 0
				work_type_Never_worked = 0
				work_type_Private = 0
				work_type_Self_employed = 0
				work_type_children = 0
				Residence_type_Urban = 0
				smoking_status_formerly_smoked = 0
				smoking_status_never_smoked = 0
				smoking_status_smokes = 0
				if(ever_married == 'Yes'):
					ever_married_Yes = 1
				if(smoking_status == 'smokes'):
					smoking_status_smokes = 1
				if(smoking_status == 'never smoked'):
					smoking_status_never_smoked = 1
				if(smoking_status == 'formerly smoked'):
					smoking_status_formerly_smoked = 1
				if(Residence_type == 'Urban'):
					Residence_type_Urban = 1
				if(work_type == 'Never_worked'):
					work_type_Never_worked = 1
				if(work_type == 'Private'):
					work_type_Private = 1
				if(work_type == 'Self-employed'):
					work_type_Self_employed = 1
				if(work_type == 'children'):
					work_type_children = 1
				if(hypertension == 'Yes'):
					hypertension_1 = 1
				if(gender == 'Male'):
					genderMale = 1
				if(heart_disease == 'Yes'):
					heart_disease_1 = 1
				dict = {
					'age' : age,
					'avg_glucose_level' : avg_glucose_level,
					'bmi' : bmi,
					'gender_Male' : genderMale,
					'hypertension_1' : hypertension_1,
					'heart_disease_1' : heart_disease_1,
					'ever_married_Yes' : ever_married_Yes,
					'work_type_Never_worked' : work_type_Never_worked,
					'work_type_Private' : work_type_Private,
					'work_type_Self-employed' : work_type_Self_employed,
					'work_type_children' : work_type_children,
					'Residence_type_Urban' : Residence_type_Urban,
					'smoking_status_formerly smoked' : smoking_status_formerly_smoked,
					'smoking_status_never smoked' : smoking_status_never_smoked,
					'smoking_status_smokes' : smoking_status_smokes

				}
				df = pd.DataFrame(dict, index=[0])
				for col in ['avg_glucose_level', 'bmi']:
					df[col] = np.log(df[col])
				mean_age = 43.226614
				std_age = 22.612647
				mean_glucose = 4.592465
				std_glucose = 0.361985
				mean_bmi = 3.328423
				std_bmi = 0.265064
				df['age'] = (df['age'] - mean_age)/(std_age)
				df['avg_glucose_level'] = (df['avg_glucose_level'] - mean_glucose)/(std_glucose)
				df['bmi'] = (df['bmi'] - mean_bmi)/(std_bmi)
				mdl=joblib.load("D:/MajorProject/HealthApp/MyAPI/brain_stroke2.pkl")
				y_pred = mdl.predict(df)
				print(y_pred)
				answer = 'No'
				if(y_pred == 1):
					answer = 'Yes'
				messages.success(request,'Risk of brain stroke ? : {}'.format(answer))

				#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
				#||||||||||||||||||||PREVIOUS CODE|||||||||||||||||||||||||||||||||||||||||||||
				# df = pd.DataFrame(dict, index=[0])
				# mdl=joblib.load("D:/MajorProject/HealthApp/MyAPI/brain_stroke2.pkl")
				# y_pred = mdl.predict(df)
				# print(y_pred)
				# answer = 'No'
				# if(y_pred == 1):
				# 	answer = 'Yes'
				# messages.success(request,'Risk of brain stroke ? : {}'.format(answer))
				#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
				#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
				
	
	form=brainStrokeForm()
				
	return render(request, 'myform/cxform.html', {'form':form})

def cxcontact2(request):
	if request.method=='POST':
		form=brainStrokeForm(request.POST)
		if form.is_valid():
				firstname = form.cleaned_data['firstname']
				lastname = form.cleaned_data['lastname']
				gender = form.cleaned_data['gender']
				age = form.cleaned_data['age']
				hypertension = form.cleaned_data['hypertension']
				heart_disease = form.cleaned_data['heart_disease']
				ever_married = form.cleaned_data['ever_married']
				work_type = form.cleaned_data['work_type']
				residence_type = form.cleaned_data['residence_type']
				avg_glucose_level = form.cleaned_data['avg_glucose_level']
				bmi = form.cleaned_data['bmi']
				myDict = (request.POST).dict()
				df=pd.DataFrame(myDict, index=[0])
				answer=approvereject(ohevalue(df))[0]
				Xscalers=approvereject(ohevalue(df))[1]
				messages.success(request,'Application Status: {}'.format(answer))
	
	form=brainStrokeForm()
				
	return render(request, 'myform/form.html', {'form':form})

	# def cxcontact(request):
	# if request.method=='POST':
	# 	form=brainStrokeForm(request.POST)
	# 	if form.is_valid():
	# 			firstname = form.cleaned_data['firstname']
	# 			lastname = form.cleaned_data['lastname']
	# 			gender = form.cleaned_data['gender']
	# 			age = form.cleaned_data['age']
	# 			hypertension = form.cleaned_data['hypertension']
	# 			heart_disease = form.cleaned_data['heart_disease']
	# 			ever_married = form.cleaned_data['ever_married']
	# 			work_type = form.cleaned_data['work_type']
	# 			residence_type = form.cleaned_data['residence_type']
	# 			avg_glucose_level = form.cleaned_data['avg_glucose_level']
	# 			bmi = form.cleaned_data['bmi']
	# 			####
	# 			gender_Male = 0
	# 			if gender == 'Male':
	# 				gender_Male = 1
	# 			hypertension_1 = 0
	# 			if hypertension == 'Yes':
	# 				hypertension_1 = 1
	# 			heart_disease_1 = 0
	# 			if heart_disease == 'Yes':
	# 				heart_disease_1 = 1
	# 			ever_married_Yes = 0
	# 			if ever_married == 'Yes':
	# 				ever_married_Yes = 1
	# 			work_type_Never_worked = 0
	# 			work_type_Private = 0
	# 			work_type_Self_employed = 0
	# 			if work_type == 'Private':
	# 				work_type_Private = 1
	# 			if work_type == 'Never worked':
	# 				work_type_Never_worked = 1
	# 			if work_type == 'Self-employed':
	# 				work_type_Self_employed = 1
				
	# 			####
	# 			myDict = (request.POST).dict()
	# 			df=pd.DataFrame(myDict, index=[0])
	# 			df.drop('csrfmiddlewaretoken', axis= 1, inplace= True)
	# 			df.drop('firstname', axis= 1, inplace= True)
	# 			df.drop('lastname', axis= 1, inplace= True)
	# 			df[['hypertension', 'heart_disease']] = df[['hypertension', 'heart_disease']].astype(str)
	# 			cat_columns=['gender','hypertension','heart_disease','ever_married','work_type', 'residence_type', 'smoking_status']
	# 			# for col in ['avg_glucose_level', 'bmi']:
	# 			# 	df[col] = np.log(df[col])
	# 			df2 = pd.get_dummies(df, columns = cat_columns)
	# 			s = StandardScaler()
	# 			df2[['bmi', 'avg_glucose_level', 'age']] = s.fit_transform(df2[['bmi', 'avg_glucose_level', 'age']])
	# 			# answer=ohevalue(df)
	# 			mdl=joblib.load("D:/MajorProject/HealthApp/MyAPI/brain_stroke2.pkl")
	# 			y_pred = mdl.predict(df2)
	# 			print(y_pred)
	# 			# print(df2)
	# 			# print(answer)
	# 			# Xscalers=approvereject(ohevalue(df))[1]
	# 			# messages.success(request,'Application Status: {}'.format(answer))
				
	
	# form=brainStrokeForm()
				
	# return render(request, 'myform/cxform.html', {'form':form})