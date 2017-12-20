from django import forms

class StandartImportForm(forms.Form):
	standartJSON = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

