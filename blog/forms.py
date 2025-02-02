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



class AdminUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter username'}),
        label="Username"
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter admin email'}),
        label="Email"
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter first name'}),
        label="First Name"
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter last name'}),
        label="Last Name"
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        user.is_admin = True
        if commit:
            user.save()
        return user


class AdminUserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Username or Email",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username or email'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        username_or_email = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username_or_email and password:
            user = authenticate(username=username_or_email, password=password)
            if user is None:
                raise forms.ValidationError("Invalid credentials.")
            if not (user.is_staff or user.is_superuser):
                raise forms.ValidationError("You do not have permission to access the admin panel.")

        return cleaned_data



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
        fields = ['name', 'email', 'phone', 'message']