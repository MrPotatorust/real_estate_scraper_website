from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class ScrapingArgsForm(forms.Form):
    buy_or_rent = forms.ChoiceField(
        choices=((1, 'Buy'), (2, 'Rent')),
    )

    type_of_property = forms.ChoiceField(
        choices=((1, 'Apartment'), (2, 'House')),
    )

    location = forms.CharField(max_length=50)