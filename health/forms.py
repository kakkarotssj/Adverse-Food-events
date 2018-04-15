from django import forms
from .models import Reg

class RegForm(forms.ModelForm):
    class Meta:
        model = Reg
        GENDER_CHOICES = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Other', 'Other'),
        )
        Gender = forms.ChoiceField(choices=GENDER_CHOICES)
        fields = ('First_Name', 'Last_Name','Gender') 