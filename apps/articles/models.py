from ckeditor.fields import RichTextField
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
    title = models.CharField(
        max_length=255, unique=True, db_index=True, verbose_name=_("Заголовок")
    )
    text = RichTextField(verbose_name=_("Полный текст ответа"))
    status = models.CharField(
        choices=ModerationStatus, default=ModerationStatus.MODERATION, verbose_name=_("Статус")
    )
    slug = AutoSlugField(populate_from="title", verbose_name=_("Ссылка"))

    class Meta:
        verbose_name = _("Статья")
        verbose_name_plural = _("Статьи")

    def __str__(self) -> str:
        return self.text[: settings.admin_preview_text]
