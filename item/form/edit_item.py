from django import forms
from django.core.validators import RegexValidator
from hashlib import md5
from jsonschema.exceptions import ValidationError

from item import models
from item.form.bootstrap import BootStrap
class ItemForm(BootStrap,forms.Form):
    gname = forms.CharField(
        label='商品名',
        widget=forms.Textarea(attrs={'rows': 6, 'cols': 40}),
        required=True,
    )
    price = forms.CharField(
        label='价格',
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        required=True,
    )
    intro_txt= forms.CharField(
        label='介绍',
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        required=True,
    )
    phone=forms.CharField(
        label='联系电话',
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        required=True,
    )

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
