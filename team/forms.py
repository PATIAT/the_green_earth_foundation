from django import forms
from .models import TeamMember
from .widgets import CustomClearableFileInput


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False, widget=CustomClearableFileInput)
