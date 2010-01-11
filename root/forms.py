from django import forms

from ibtsocs.root.models import Post

class PostForm(forms.ModelForm):
    def clean_message(self):
        message = self.cleaned_data['message']
        if not message.rstrip(' .').lower().endswith('ibtsocs'):
            raise forms.ValidationError("Are you sure you're on the right site? All posts must end with IBTSOCS.")

        return message

    class Meta:
        model = Post
        fields = ['message', 'nick']
