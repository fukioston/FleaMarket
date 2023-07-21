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

list = models.Items.objects.all()
ran = []
i = 0
while True:
    rn = randint(0, len(list) - 1)
    if rn not in ran:
        ran.append(rn)
        i = i + 1
    if i == 12:
        break
    finlist=[]
    for r in ran:
        finlist.append(list[int(r)])
print(finlist)
