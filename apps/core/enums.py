from django.db import models
from django.utils.translation import gettext_lazy as _


class ModerationStatus(models.TextChoices):
    """Enums со статусом модерации"""

    MODERATION = ("MODERATION", _("Модерация"))
    PUBLIC = ("PUBLIC", _("Опубликован"))
    DECLINED = ("DECLINED", _("Отклонен"))
