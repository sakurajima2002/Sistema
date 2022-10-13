from django import forms

from boss.models import Boss

class Boss_Form(forms.ModelForm):
    class Meta:
        model = Boss
        fields = ['first_name', 'last_name', 'email', 'salary', 'phone', 'dni', 'image', 'boss_area']