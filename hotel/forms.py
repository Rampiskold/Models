# -*- coding: utf-8 -*-
from django import forms

from .models import *


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        exclude = [""]

