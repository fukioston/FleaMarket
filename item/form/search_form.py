from django import forms
from django.core.validators import RegexValidator

from user.forms.bootstrap import BootStrap


class SearchForm(BootStrap, forms.Form):
    search_field = forms.CharField(
        label='搜索',
        widget=forms.TextInput(),
        required=True
    )

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
