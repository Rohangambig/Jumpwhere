from django import forms
from .models import shortURL

class URLForm(forms.ModelForm):
    class Meta: 
        model =  shortURL 
        fields = ['original_url']