from django import forms

class GetNewsForm(forms.Form):
    api_key = forms.CharField(label='API Key', required=False, widget=forms.TextInput(attrs={'size': '40'}))