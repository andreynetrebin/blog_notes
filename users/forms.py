from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):

    def __init__(self, *arqs, **kwarqs):
        super(UserCreationForm, self).__init__(*arqs, **kwarqs)
        self.fields['email'].required = True

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('sfr.gov.ru'):
            raise forms.ValidationError('Пожалуйста введите почтовый ящик АРМ ГС')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже зарегистрирован')
        return email
    
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
        