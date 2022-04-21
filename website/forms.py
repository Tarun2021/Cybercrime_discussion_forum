from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Question,Response,Audio
from django import forms
class RegUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={
            'email': forms.EmailInput(attrs={
                'required': True,
                'placeholder': 'abc@xyz.com',
                'autofocus': True
            }),
            'username': forms.TextInput(attrs={
                'placeholder': 'testcase',
            })
        }


def __init__(self, *args, **kwargs):
        super(RegUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs = {'placeholder': 'password'}
        self.fields['password2'].widget.attrs = {'placeholder': 'confirm password'}        

class Loginform(AuthenticationForm):
    class Meta:
        fields="_all_"

class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={
                'autofocus': True,
                'placeholder': 'How to ensure women and children safety?'
            })
        }        

class NewResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['body']

class NewReplyForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'What do you have to say for this?'
            })
        }  
'''                  
class AudioForm(forms.ModelForm):
    class Meta:
        model=Audio
        fields=['record']        
        '''