
from django import forms

class KeywordForm(forms.Form):
    keyword = forms.CharField(label='事件关键词', max_length=100)
