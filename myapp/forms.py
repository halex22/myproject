from .models import Profile
from django.forms import ModelForm
from django.forms.widgets import TextInput, Input


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        exclude = ["sing_up_date"]
        error_messages = {
            "name": {
                "required": "Name can not be empty"
            }
        }
        widgets = {
            "name": TextInput(attrs={"class": "input-element form-control"})
        }
        labels = {
            "name": "Username",
            "profile_pic": "Profile Picture"
        }
