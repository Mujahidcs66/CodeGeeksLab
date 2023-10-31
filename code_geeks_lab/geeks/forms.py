from django import forms 
from .models import GeeksModel

class GeeksForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    
class GeeksModelForm(forms.ModelForm):
    
    class Meta:
        model = GeeksModel
        exclude = ['last_modified',]