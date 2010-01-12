from django import forms
from django.conf import settings
from django.forms import widgets

from ibtsocs.root.models import Post
from ibtsocs.root.fields import ReCaptchaField

class PostForm(forms.ModelForm):
    message = forms.CharField(
        max_length=255,
        label="Why are you bemoaning computer science today?",
        required=True,
        widget=widgets.Textarea,
        )
    if getattr(settings, 'RECAPTCHA', True):
        recaptcha = ReCaptchaField()

    def clean_message(self):
        message = self.cleaned_data['message']
        if not message.rstrip(' .').lower().endswith('ibtsocs'):
            raise forms.ValidationError("Are you sure you're on the right site? All posts must end with IBTSOCS.")

        return message

    class Meta:
        model = Post
        fields = ['message', 'nick']
