from typing import TypeVar

from django.contrib import messages
from django.db import models
from django.db.models import QuerySet
from django.http import HttpRequest
from django.utils.html import strip_tags

from config.config import settings
from core.enums import ModerationStatus


class AdminMixin:
    ModelType = TypeVar("ModelType", bound=models.Model)

    def short_text(
        self,
        model: ModelType,
        method_name: str = "text",
        text_limit: int | None = settings.admin_preview_text_limit,
    ) -> str:
        """
        Удаляет html теги из текста и возвращает урезанный текст по количеству символов
        """
        text_original = getattr(model, method_name, None)

        if not text_original:
            raise AttributeError(
                f"Атрибут {method_name} не найден в модели {model.__class__.__name__}"
            )

        text_without_html_tags: str = strip_tags(text_original)
        return text_without_html_tags[:text_limit] if text_limit else text_without_html_tags

    @staticmethod
    def _message_user(request: HttpRequest, message: str, level: int = messages.INFO) -> None:
        messages.add_message(request, level, message)

    def set_public(self, request: HttpRequest, queryset: QuerySet) -> None:
        count: int = queryset.update(status=ModerationStatus.PUBLIC)
        self._message_user(request, f"{count} записей опубликованы.")

    def set_declined(self, request: HttpRequest, queryset: QuerySet) -> None:
        count: int = queryset.update(status=ModerationStatus.DECLINED)
        self._message_user(request, f"{count} записей сняты с публикации!")
