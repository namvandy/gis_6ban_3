from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreatetionForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

