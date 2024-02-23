from django.db import models

from Utils.models import CommonDataAbstractModel
from Utils.slug import AutoSlugField


class Company(CommonDataAbstractModel):
    """Модель компании"""

    name = models.CharField(max_length=255, unique=True, db_index=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    def questions(self):
        return self.question_set.all()

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
