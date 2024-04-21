from django import forms


class TaskCreationForm(forms.Form):
    title = forms.CharField(label='title', max_length=255)
    content = forms.CharField(label='content', widget=forms.Textarea())
