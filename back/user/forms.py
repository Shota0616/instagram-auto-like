from django import forms
from django.contrib.auth.models import User

from allauth.account.forms import SignupForm

from .models import MyUser


# フォームクラス作成
class UserForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','email','password')
        # フィールド名指定
        labels = {'username':"ユーザー名",'email':"Eメール"}

class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='姓')
    last_name = forms.CharField(max_length=30, label='名')

class SignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='姓')
    last_name = forms.CharField(max_length=30, label='名')

    def save(self, request):
        user = super(SignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user