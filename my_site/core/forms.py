from django import forms


class Programmer(forms.Form):
    message_to_print = forms.CharField(max_length=100)