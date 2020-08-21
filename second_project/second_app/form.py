from django import forms
from second_app.models import  user

# class FormName(forms.Form):

class user_form(forms.ModelForm):

    class Meta():
        model = user
        fields = '__all__'

