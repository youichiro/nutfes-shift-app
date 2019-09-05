from django import forms


class NotificationForm(forms.Form):
    title = forms.CharField(
        label='タイトル',
        max_length=100,
        required=True
    )
    body = forms.CharField(
        label='本文',
        widget=forms.Textarea,
        required=True
    )
