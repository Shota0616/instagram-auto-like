from django import forms
from django.contrib.auth.models import User

from allauth.account.forms import SignupForm, LoginForm, ResetPasswordForm, ResetPasswordKeyForm

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


# allauthForm
class MyCustomSignupForm(SignupForm):
    # class Meta:
    #     model = MyUser
    #     fields = ['first_name', 'last_name', 'profile_image',]
    first_name = forms.CharField(max_length=30, label='姓')
    last_name = forms.CharField(max_length=30, label='名')
    profile_image = forms.ImageField(required=False)

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.profile_image = self.cleaned_data['profile_image']
        user.save()
        return user

# class LoginForm(LoginForm):
#     pass

# class ResetPasswordForm(ResetPasswordForm):
#     pass


# class ResetPasswordKeyForm(ResetPasswordKeyForm):
#     pass

# class ChangePasswordForm(authforms.ChangePasswordForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'

#     oldpassword = authforms.PasswordField(
#         label=("Current Password"), autocomplete="current-password"
#     )
#     password1 = authforms.SetPasswordField(label=("New Password"))
#     password2 = authforms.PasswordField(label=("New Password (again)"))

#     def __init__(self, *args, **kwargs):
#         super(ChangePasswordForm, self).__init__(*args, **kwargs)
#         self.fields["password1"].user = self.user

#     def clean_oldpassword(self):
#         if not self.user.check_password(self.cleaned_data.get("oldpassword")):
#             raise forms.ValidationError(("Please type your current password."))
#         return self.cleaned_data["oldpassword"]

#     def save(self):
#         get_adapter().set_password(self.user, self.cleaned_data["password1"])