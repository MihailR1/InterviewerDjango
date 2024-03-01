from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel

from django.db import models
from django.utils.translation import gettext_lazy as _

from config.config import settings
from config.settings import AUTH_USER_MODEL
from core.enums import ModerationStatus
from core.models import SlugModel


class Article(SlugModel, TimeStampedModel, models.Model):
    """Статья с полным разбором вопроса"""

    user = models.ForeignKey(
        AUTH_USER_MODEL, models.SET_DEFAULT, default=1, verbose_name=_("Пользователь")
    )
    text = models.TextField(verbose_name=_("Полный текст ответа"))
    slug = AutoSlugField(populate_from="text", verbose_name=_("Ссылка"))
    status = models.CharField(
        choices=ModerationStatus, default=ModerationStatus.MODERATION, verbose_name=_("Статус")
    )

    class Meta:
        verbose_name = _("Статья")
        verbose_name_plural = _("Статьи")

    def __str__(self) -> str:
        return self.text[: settings.admin_preview_text]
