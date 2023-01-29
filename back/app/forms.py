from django import forms

class InstaAutoForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
        attrs={'type':'email', 'name':'login', "autocomplete":"email", 'placeholder':'メールアドレス', 'class':'form-control'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
        attrs={'type':'password', 'placeholder':'パスワード', 'class':'form-control'}))
    num_of_times = forms.IntegerField(
        widget=forms.TextInput(
        attrs={'placeholder':'繰り返し回数', 'class':'form-control'}))