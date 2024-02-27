from django.db import models
from django.utils.translation import gettext_lazy as _

from config.settings import AUTH_USER_MODEL
from core.models import CommonDataAbstractModel
from core.slug import AutoSlugField


class Article(CommonDataAbstractModel):
    """Статья с полным разбором вопроса"""

    user = models.ForeignKey(
        AUTH_USER_MODEL, models.SET_DEFAULT, default=1, verbose_name=_("Пользователь")
    )
    text = models.TextField(verbose_name=_("Полный текст ответа"))
    slug = AutoSlugField(populate_from="text", unique=True, verbose_name=_("Ссылка"))

    class Meta:
        verbose_name = _("Статья")
        verbose_name_plural = _("Статьи")
