from django import forms
from .models import Header, Menu, Slider

class HeaderForm(forms.ModelForm):
    class Meta:
        model = Header
        fields = ['logo']



class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['menu']


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['image', 'title', 'title_continue', 'text', 'last']