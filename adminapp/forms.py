from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from authapp.forms import forms


class AdminShopUserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username', 'first_name', 'last_name', 'is_superuser',
            'is_staff', 'password1', 'password2',
            'email', 'age', 'avatar'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Пользователь слишком молод!")
        return data

    # def clean_avatar(self):
    #     pass
