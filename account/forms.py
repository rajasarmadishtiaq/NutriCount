from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo', 'weight', 'height', 'exercise', 'age', 'gender', 'preference')

    def save(self, commit=True):
        profile = super().save(commit=False)
        weight = profile.weight
        height = profile.height
        exercise = profile.exercise
        age = profile.age
        preference = profile.preference
        gender = profile.gender

        if weight and height and exercise and age and preference and gender == 'Male':
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
            calorie = bmr * exercise + preference
            profile.calorie = calorie

        elif weight and height and exercise and age and preference and gender == 'Female':
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
            calorie = bmr * exercise + preference
            profile.calorie = calorie

        else:
            profile.calorie = None

        if commit:
            profile.save()

        return profile
