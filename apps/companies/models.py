from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel

from django.db import models
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _

from core.models import SlugModel


class Company(SlugModel, TimeStampedModel, models.Model):
    """Модель компании"""

    name = models.CharField(max_length=255, unique=True, db_index=True, verbose_name=_("Компания"))
    slug = AutoSlugField(populate_from="name", editable=True, verbose_name=_("Ссылка"))

    class Meta:
        verbose_name = _("Компания")
        verbose_name_plural = _("Компании")

    def questions(self) -> QuerySet:
        return self.question_set.all()

    def __str__(self) -> str:
        return self.name
