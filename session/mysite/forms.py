# -*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
    CITY = [
        ['bj','北京'],
        ['sh','上海'],
        ['gz','广州'],
        ['sz','深圳'],
        ['hz','杭州'],
        ['ly','洛阳'],
    ]
    user_name = forms.CharField(label='你的姓名',max_length=50,initial='小小佳')
    user_city = forms.ChoiceField(label='居住城市',choices=CITY)
    user_school = forms.BooleanField(label='是否在学',required=False)
    user_email = forms.EmailField(label='电子邮件')
    user_message = forms.CharField(label='你的意见',widget=forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField(label='姓名',max_length=10)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())