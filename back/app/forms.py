from django import forms

class InstaAutoForm(forms.Form):
    insta_email = forms.EmailField(
        widget=forms.TextInput(
        attrs={'type':'email', 'name':'login', "autocomplete":"email", 'placeholder':'メールアドレス', 'class':'form-control'}))
    insta_password = forms.CharField(
        widget=forms.PasswordInput(
        attrs={'type':'password', 'placeholder':'パスワード', 'class':'form-control'}))
    insta_num_of_times = forms.IntegerField(
        widget=forms.TextInput(
        attrs={'placeholder':'繰り返し回数', 'class':'form-control'}))