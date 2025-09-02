from django import forms
from .models import Contactmessage


class Contactform(forms.ModelForm):
    class Meta:
        model = Contactmessage
        fields = ["name", "email","subject","message"]


        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Type your message'}),
        }




