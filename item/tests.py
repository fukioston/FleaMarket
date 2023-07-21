from django.test import TestCase
from django.test import TestCase

# Create your tests here.
import os

"""Run administrative tasks."""
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysiteorm.settings')
import django

django.setup()

from . import models
from random import *

with open('utils/datas.json', encoding="utf-8", errors="ignore") as fr:
    import json

    datas = json.load(fr)

    for data in datas:
        models.Items.objects.create(gname=data['gname'], userid=data['userid'], price=data['price'],
                             intro_txt=data['intro_txt'], img_index=data['img_index'])
