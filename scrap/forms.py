from django import forms


class UserForm(forms.Form):
    search = forms.CharField(label='Поиск', widget=forms.TextInput(attrs={"class": "myfield"}))
    # name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={"class": "myfield"}))
    # age = forms.IntegerField(label='Возраст', widget=forms.NumberInput(attrs={"class": "myfield"}))
    # name = forms.CharField(label='Имя', min_length=3)
    # age = forms.IntegerField(label='Возраст', min_value=1, max_value=100)
    # required_css_class = "field"
    # error_css_class = "error"
    # name = forms.GenericIPAddressField(label='Имя', min_length=3) # , help_text="Введите свое имя"
    # age = forms.IntegerField(label='Возраст', initial=18) # , help_text="Введите свой возраст"
    # comment_change = forms.CharField(widget=forms.Textarea, label='Коммент')
    # field_order = ["comment_change", "age", "name"]
