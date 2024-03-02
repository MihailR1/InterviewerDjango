from ckeditor.fields import RichTextField
from django_extensions.db.models import TimeStampedModel

from django.db import models
from django.utils.translation import gettext_lazy as _

from config.config import settings
from config.settings import AUTH_USER_MODEL


class Comment(TimeStampedModel, models.Model):
    """Модель комментария к вопросу"""

    user = models.OneToOneField(
        AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Пользователь")
    )
    text = RichTextField(verbose_name=_("Текст комментария"))

    class Meta:
        verbose_name = _("Комментарий")
        verbose_name_plural = _("Комментарии")

    def __str__(self) -> str:
        return self.text[: settings.admin_preview_text]
