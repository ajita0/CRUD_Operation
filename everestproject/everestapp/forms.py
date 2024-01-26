from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget
class ClientNewsCreateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control',
            }
            ),
            'category':forms.Select(),
            #'content':forms.Textarea(attrs={
            # 'class':'form-control summernote',
            # }),
            'content':SummernoteWidget(),
            'image':forms.ClearableFileInput(),
        }

class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder':"username...",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
    'class': 'form-control',
    'placeholder':"password",   
    }))