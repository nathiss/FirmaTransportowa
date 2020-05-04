from django import forms


class CreatePortForm(forms.Form):
    title = forms.CharField(max_length=100, label='Tytuł artykułu')
    content = forms.CharField(label='Treść artykułu', widget=forms.Textarea)
