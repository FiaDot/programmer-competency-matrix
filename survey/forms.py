from django.forms import ModelForm

from survey.models import User


class UserForm(ModelForm):
    class Meta:
        model = User        
        exclude = ["post"]