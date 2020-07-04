from django.forms import Form
from django import forms
from tinymce.widgets import TinyMCE

class RichForm(Form):
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows':50,'class': 'form-control'}),required=False,label="Text")