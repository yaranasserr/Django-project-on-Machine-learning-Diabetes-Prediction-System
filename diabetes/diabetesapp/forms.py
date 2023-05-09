from django import forms

class PredictionForm(forms.Form):
    pregnancies = forms.IntegerField()
    glucose = forms.IntegerField()
    blood_pressure = forms.IntegerField()
    skin_thickness = forms.IntegerField()
    insulin = forms.IntegerField()
    bmi = forms.FloatField()
    diabetes_pedigree_function = forms.FloatField()
    age = forms.IntegerField()