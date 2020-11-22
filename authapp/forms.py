import hashlib

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
import django.forms as forms
from django.utils.crypto import random

from authapp.models import ShopUser, ShopUserProfile


class ShopUserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
            field.help_text = ''

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return age

    def save(self, **kwargs):
        user = super(ShopUserRegisterForm, self).save()

        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf-8')).hexdigest()
        # print('=='*200, user.activation_key, '=='*200, user.email)
        user.save()

        return user


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = (
            'username', 'first_name', 'last_name',
            'email', 'avatar', 'age'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return age

class ShopUserProfileEditForm(UserChangeForm):
    class Meta:
        model = ShopUserProfile
        fields = (
            'tagline', 'about_me', 'gender',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
