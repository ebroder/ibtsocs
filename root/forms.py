import re

from django import forms
from django.conf import settings
from django.forms import widgets

from ibtsocs.root.models import Post
from ibtsocs.root.fields import ReCaptchaField

POST_RE = re.compile(r'ibtso[a-z]*\.?$', re.I)

class PostForm(forms.ModelForm):
    message = forms.CharField(
        max_length=255,
        label="Why are you bemoaning computer science today?",
        required=True,
        widget=widgets.Textarea,
        )
    if hasattr(settings, 'RECAPTCHA_PUBLIC_KEY'):
        recaptcha = ReCaptchaField()

    def clean_message(self):
        message = self.cleaned_data['message']
        if not POST_RE.search(message):
            raise forms.ValidationError("Are you sure you're on the right site? All posts must end with IBTSOCS.")

        return message

    class Meta:
        model = Post
        fields = ['message', 'nick']
