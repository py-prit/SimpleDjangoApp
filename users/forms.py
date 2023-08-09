from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import UserUploadedData, User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UserUploadedData
        fields = ['name', 'file']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(FileUploadForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        data = super().save(commit=False)
        data.user = self.user
        data.save()
