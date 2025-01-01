
f# scraper/forms.py
from django import forms

class KeywordForm(forms.Form):
    keyword = forms.CharField(label='请输入事件关键词', max_length=100)

class IDForm(forms.Form):
    id = forms.CharField(label='请输入小红书ID', max_length=50)