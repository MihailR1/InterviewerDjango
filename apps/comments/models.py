from django.db import models
from django.utils.translation import gettext_lazy as _

from config.settings import AUTH_USER_MODEL
from core.models import CommonDataAbstractModel


class Comment(CommonDataAbstractModel):
    """Модель комментария к вопросу"""

    user_id = models.OneToOneField(
        AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Пользователь")
    )
    text = models.TextField(verbose_name=_("Текст комментария"))

    class Meta:
        verbose_name = _("Комментарий")
        verbose_name_plural = _("Комментарии")
