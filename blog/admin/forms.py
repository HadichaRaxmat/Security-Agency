from django import forms
from blog.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate



TABLE_CHOICES = [
    ('user_contact', 'User Contact'),
    ('header', 'Header'),
    ('menu', 'Menu'),
    ('header_touch', 'Header Touch'),
    ('slider', 'Slider'),
    ('about', 'About'),
    ('service_header', 'Service Header'),
    ('service', 'Service'),
    ('client', 'Client'),
    ('touch', 'Touch'),
    ('team', 'Team'),
    ('guard', 'Guard'),
    ('info', 'Info'),
    ('contact_us', 'Contact Us'),
    ('subscribe', 'Subscribe'),
    ('footer', 'Footer'),
]

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
    role = forms.ChoiceField(
        choices=CustomUser.ROLE_CHOICES,
        label="Role",
        required=True
    )
    allowed_tables = forms.MultipleChoiceField(
        choices=TABLE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Allowed Tables"
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'password1', 'password2', 'allowed_tables']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        user.is_admin = user.role in ['admin', 'admin_manager', 'superuser']

        if isinstance(user.allowed_tables, list):
            user.allowed_tables = ','.join(self.cleaned_data['allowed_tables'])

        if commit:
            user.save()
        return user



class AdminUserUpdateForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter new password (optional)'}),
        required=False,
        label="New Password"
    )

    allowed_tables = forms.MultipleChoiceField(
        choices=TABLE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Allowed Tables"
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'allowed_tables']

    def save(self, commit=True):
        user = super().save(commit=False)

        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])

        if isinstance(user.allowed_tables, list):
            user.allowed_tables = ','.join(self.cleaned_data['allowed_tables'])

        if commit:
            user.save()
        return user



class AdminUserAuthenticationForm(forms.Form):  # Заменили AuthenticationForm на forms.Form
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
        identifier = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not identifier or not password:
            raise forms.ValidationError("Invalid credentials.")

        user = None
        if CustomUser.objects.filter(email=identifier).exists():
            user = CustomUser.objects.get(email=identifier)
        elif CustomUser.objects.filter(username=identifier).exists():
            user = CustomUser.objects.get(username=identifier)

        if user:
            authenticated_user = authenticate(username=user.email, password=password)
            if authenticated_user is None:
                raise forms.ValidationError("Invalid credentials.")
            elif not (authenticated_user.is_staff or authenticated_user.is_superuser):
                raise forms.ValidationError("You do not have permission to access the admin panel.")
        else:
            raise forms.ValidationError("Invalid credentials.")

        return cleaned_data


class AvatarUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar']


class AdminProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'avatar']



