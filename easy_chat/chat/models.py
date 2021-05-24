import reprlib

from django.db import models
from django.utils.translation import gettext_lazy as _


class Message(models.Model):
    username = models.CharField(
        _("user"),
        max_length=50,
        blank=False,
        null=False,
        help_text=_("Username of the person who sent a message"),
    )
    text = models.CharField(
        _("text"),
        max_length=500,
        blank=False,
        null=False,
        help_text=_("Text of a messages"),
    )
    timestamp = models.DateTimeField(
        _("timestamp"),
        null=False,
        auto_now=False,
        auto_now_add=True,
        help_text=_("Timestamp of a message"),
    )

    class Meta:
        verbose_name = _("message")
        verbose_name_plural = _("messages")

    def __str__(self):
        _text = reprlib.repr(self.text)
        return f"[{self.timestamp:'%d/%m/%y %H:%M'}] {self.username} {_text}"

    def to_dict(self):
        return {
            "username": self.username,
            "text": self.text,
            "timestamp": self.timestamp.isoformat(),
        }
