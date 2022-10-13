from django import forms

from workArea.models import Work_Area 

class Work_Area_Form(forms.ModelForm):
    class Meta:
        model = Work_Area
        fields = ['name']