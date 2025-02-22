from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Header, Menu, Slider, About, ServiceHeader, Service, Client, Touch, Team, Guard, Info, ContactUs, \
    Subscribe, Footer, UserContact, CustomUser



class CustomUserCreationUserForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'})
    )


    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')
        exclude = ('username',)



class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )

    class Meta:
        email = forms.EmailField(required=True,
                                 widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address'}))
        model = CustomUser
        fields = ('username', 'password')



class UserContactForm(forms.ModelForm):
    class Meta:
        model = UserContact
        fields = ['name', 'email', 'phone', 'message']

class HeaderForm(forms.ModelForm):
    class Meta:
        model = Header
        fields = ['logo']



class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ["title", "menu", "is_active"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["menu"].widget = forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"})
        self.fields["title"].widget = forms.TextInput(attrs={"class": "form-control"})
        self.fields["is_active"].widget = forms.CheckboxInput(attrs={"class": "form-check-input"})



class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['image', 'title', 'title_continue', 'text', 'last']


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['image', 'title', 'text', 'last']


class ServiceHeaderForm(forms.ModelForm):
    class Meta:
        model = ServiceHeader
        fields = ['title']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'text', 'last']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['image', 'name', 'title', 'text']


class TouchForm(forms.ModelForm):
    class Meta:
        model = Touch
        fields = ['title', 'last', 'image']


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['title', 'text', 'last']


class GuardForm(forms.ModelForm):
    class Meta:
        model = Guard
        fields = ['name', 'status', 'image']


class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['title', 'text']


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['title']


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['title', 'email', 'last']


class FooterForm(forms.ModelForm):
    class Meta:
        model = Footer
        fields = ['info']


class UserContactForm(forms.ModelForm):
    class Meta:
        model = UserContact
        fields = ['name', 'email', 'phone', 'message', 'status']