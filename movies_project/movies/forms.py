from .models import Comment, Movie
from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(required=True, max_length=20,
                           widget=forms.widgets.TextInput(), )

    comment = forms.CharField(required=True,
                              widget=forms.widgets.Textarea(), )


class SearchForm(forms.Form):
    title = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(
                                attrs={
                                    "placeholder": "Search by movie title....",
                                    "class": "text-center"
                                }
                            ), label=False)
