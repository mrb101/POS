from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", required=True, max_length=30,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'name': 'username'}))
    password = forms.CharField(label="Password", required=True, max_length=30,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'name': 'password'}))


class OrderForm(forms.Form):
    product = forms.CharField(label="Product", required=True, max_length=255,
                              widget=forms.TextInput(attrs={
                                  'class': 'form-control',
                                  'name': 'product'}))
    quantity = forms.IntegerField(label="Quantity", required=True,
                                  widget=forms.NumberInput(attrs={
                                      'class': 'form-control',
                                      'name': 'quantity'}))
    discount = forms.IntegerField(label="Discount", required=False,
                                  widget=forms.NumberInput(attrs={
                                      'class': 'form-control',
                                      'name': 'discount'}))
    notes = forms.CharField(label="notes", required=True, max_length=255,
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'name': 'notes'}))


class PaymentForm(forms.Form):
    type = forms.CharField(label="Type", required=True, max_length=100,
                              widget=forms.TextInput(attrs={
                                  'class': 'form-control',
                                  'name': 'type'}))
    cash = forms.IntegerField(label="Cash", required=False,
                              widget=forms.NumberInput(attrs={
                                  'class': 'form-control',
                                  'name': 'cash'}))
