from django import forms
from cowsay_app.models import CowMessages


class PrintMessageForm(forms.Form):
    text = forms.CharField(max_length=150)
