from django import forms
from django.utils.translation import ugettext_lazy as _

# from .models import Message


class UsernameForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=50,
        strip=True,
        required=True,
        label=_("Username"),
        help_text=_("How we can call you in chat?"),
    )
