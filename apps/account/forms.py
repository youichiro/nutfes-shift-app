from django import forms
from django.contrib.auth import password_validation
from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='パスワード',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='パスワード(確認)',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='上のパスワードをもう一度入力してください.',
    )

    class Meta:
        model = User
        fields = ('name', 'email')
        labels = {
            'name': '名前',
            'email': 'メールアドレス'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
