from .models import shop
from django import forms


class modelform(forms.ModelForm):
    class Meta:
        model=shop
        fields=['name','price','desc','img']

    