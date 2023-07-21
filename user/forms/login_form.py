from django import forms
from django.core.validators import RegexValidator
from hashlib import md5
from jsonschema.exceptions import ValidationError

from user import models
from user.forms.bootstrap import BootStrap


class LoginForm(BootStrap, forms.Form):
    mobile_phone = forms.CharField(
        label='手机号',
        widget=forms.TextInput(),
        required=True,

        validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式不正确'), ]
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(),
        required=True,

    )

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    # def clean_password(self):
    #     pw = self.cleaned_data.get('password')
    #     return md5(pw.encode()).hexdigest()
