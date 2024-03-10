from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ShippingAddress, Payment
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=('username','email','password1','password2')


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields=('username','password')


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['first_name', 'last_name', 'city', 'country', 'postal_code']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['name_on_card', 'card_number', 'expiry_date', 'security_code', 'zip_code']
