from django.forms import ModelForm

from django.forms import TextInput
from django.forms import EmailInput
from django.forms import NumberInput

from survey.models import User


class UserForm(ModelForm):
    class Meta:
        model = User        
                
        widgets = {            
            'name' : TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'email' : EmailInput(attrs={'class':'form-control','placeholder':'Email'}),            
            'exp' : NumberInput(attrs={'class':'form-control','placeholder':'0'}),             
        }
                 
        
        exclude = ["post"]