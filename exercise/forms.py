from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('model_year', 'make', 'model', 'rejection_percentage', 'reason_1', 'reason_2', 'reason_3', )