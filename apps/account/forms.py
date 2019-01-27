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
        fields = ('student_id', 'name', 'belong', 'department', 'grade', 'phone_number')
        labels = {
            'student_id': '学籍番号',
            'name': '名前',
            'belong': '局・部門',
            'department': '学科',
            'grade': '学年',
            'phone_number': '電話番号',
        }
        widgets = {
            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'belong': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'grade': forms.Select(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        # ここで学籍番号のバリデーションを書く
        if len(student_id) != 8:
            raise forms.ValidationError('学籍番号が正しくありません.')
        return student_id

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if len(phone_number) != 11:
            raise forms.ValidationError('電話番号が正しくありません.')
        return phone_number

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('パスワードが一致しません.')
        return password2

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
