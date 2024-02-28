import pytils

from django.db import models


class SlugModel(models.Model):
    """Переводит url в кириллицу

    На уровне модели указать поле по которому будет строиться slug
    slug = AutoSlugField(populate_from="title", verbose_name=_("Ссылка"))
    """

    @staticmethod
    def slugify_function(content: str) -> str:
        return pytils.translit.slugify(content)

    class Meta:
        abstract = True
