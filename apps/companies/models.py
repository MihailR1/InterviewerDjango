from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import CommonDataAbstractModel
from core.slug import AutoSlugField


class Company(CommonDataAbstractModel):
    """Модель компании"""

    name = models.CharField(max_length=255, unique=True, db_index=True, verbose_name=_("Компания"))
    slug = AutoSlugField(populate_from="name", unique=True, verbose_name=_("Ссылка"))

    def questions(self):
        return self.question_set.all()

    class Meta:
        verbose_name = _("Компания")
        verbose_name_plural = _("Компании")
