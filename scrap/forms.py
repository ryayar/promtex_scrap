from django import forms


class UserForm(forms.Form):
    search = forms.CharField(label='Поиск', widget=forms.TextInput(attrs={"class": "myfield"}))
