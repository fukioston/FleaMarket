from django import forms
from django.conf import settings
from django.http import HttpResponse

from user import models
from utils.tencent.sms import send_sms_single
import random
from user.forms.bootstrap import BootStrap
# class LoginSmsForm(BootStrap,forms.ModelForm):
