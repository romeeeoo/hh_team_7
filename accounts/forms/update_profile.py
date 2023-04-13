from django import forms

from accounts.models import Profile


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'phone_number']
