from django import forms

class ScraperForm(forms.Form):
    keyword = forms.CharField(max_length=255, label='事件关键词')
    xhs_id = forms.CharField(max_length=255, label='小红书ID')
