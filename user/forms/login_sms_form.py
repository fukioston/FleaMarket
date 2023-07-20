from django import forms
from django.conf import settings
from django.core.validators import RegexValidator
from django.http import HttpResponse

from user import models
from utils.tencent.sms import send_sms_single
import random
from user.forms.bootstrap import BootStrap
class LoginSmsForm(BootStrap,forms.Form):
    mobile_phone = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式不正确'), ]
    )
    code = forms.CharField(
        label='验证码',
        widget=forms.TextInput())
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
