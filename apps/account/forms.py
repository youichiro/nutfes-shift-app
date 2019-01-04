from django import forms
from django.contrib.auth import password_validation
from .models import User


BELONG_CHOICES = (
    ('総務局', '総務局'),
    ('企画局', '企画局'),
    ('制作局', '制作局'),
    ('渉外局', '渉外局'),
    ('財務局', '財務局'),
)

DEPARTMENT_CHOICES = (
    ('機械', '機械'),
    ('電気', '電気'),
    ('物材', '物材'),
    ('環社', '環社'),
    ('生物', '生物'),
    ('情経', '情経'),
    ('原子力', '原子力'),
    ('システム安全', 'システム安全'),
)

GRADE_CHOICES = (
    ('B1', 'B1'),
    ('B2', 'B2'),
    ('B3', 'B3'),
    ('B4', 'B4'),
    ('M1', 'M1'),
    ('M2', 'M2'),
    ('D1', 'D1'),
    ('D2', 'D2'),
    ('D3', 'D3'),
)


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
    belong = forms.ChoiceField(
        label='所属',
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=BELONG_CHOICES,
        help_text='兼局している場合はメインの部門を選択してください.'
    )
    department = forms.ChoiceField(
        label='学科',
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=DEPARTMENT_CHOICES,
    )
    grade = forms.ChoiceField(
        label='学年',
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=GRADE_CHOICES,
    )

    class Meta:
        model = User
        fields = ('student_id', 'name', 'belong', 'department', 'grade', 'phone_number')
        labels = {
            'student_id': '学籍番号',
            'name': '名前',
            'phone_number': '電話番号',
        }
        widgets = {
            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
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
