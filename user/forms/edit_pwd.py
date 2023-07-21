from django import forms

from user.forms.bootstrap import BootStrap


class PwdForm(BootStrap, forms.Form):
    old_pwd=forms.CharField(
        label='旧密码',
        widget=forms.TextInput(),
        required=True,
    )
    new_pwd=forms.CharField(
        label='新密码',
        widget=forms.TextInput(),
        required=True,
    )
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request