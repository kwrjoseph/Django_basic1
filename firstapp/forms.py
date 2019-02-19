from django import forms
from django.core import validators
from django.contrib.auth.models import User
from firstapp.models import UserProfileInfo


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


class UserForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter you email again:')
    password = forms.CharField(widget=forms.PasswordInput())
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    class Meta:
        model = User
        fields = ('username', 'name', 'email')


    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('check email')

# custom validator
# def clean_botcatcher(self):
#     botcatcher = self.cleaned_data['botcatcher']
#     if len(botcatcher) > 0:
#         raise forms.ValidationError("got you bot")
#     return botcatcher


# models form
# class NewUser(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'

# custom validator
# def clean_botcatcher(self):
#     botcatcher = self.cleaned_data['botcatcher']
#     if len(botcatcher) > 0:
#         raise forms.ValidationError("got you bot")
#     return botcatcher
