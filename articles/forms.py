#!/usr/bin/env python
# -*- coding:utf-8 -*-

# form表单验证

from django import forms
from .models import GetMessage


class GetMessageForm(forms.ModelForm):
    """读者留言验证,注意这里继承的是ModelForm"""

    class Meta:
        """继承GetMessage类"""
        model = GetMessage
        fields = ['name', 'email', 'subject', 'message']
