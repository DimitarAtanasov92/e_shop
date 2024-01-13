from django import forms

from e_shop.events.models import CommentEvent


class CommentEventForm(forms.ModelForm):

    class Meta:
        model = CommentEvent
        fields = ['comment']
