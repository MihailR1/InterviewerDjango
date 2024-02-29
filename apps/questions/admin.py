from django.contrib import admin, messages
from django.db.models import QuerySet
from django.http import HttpRequest

from config.config import settings
from questions.models import Category, Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "short_text", "level", "status", "created")
    list_display_links = ("title",)
    list_editable = ("status",)
    list_per_page = settings.admin_elements_per_page

    ordering = ["-created", "title"]
    actions = ["set_public", "set_declined"]
    search_fields = ["title", "text"]
    list_filter = ["status", "created", "categories__name", "companies__name"]

    fields = ["title", "slug", "status", "level", "text", "answer", "categories", "companies"]
    readonly_fields = ["slug"]
    filter_horizontal = ["categories", "companies"]
    save_on_top = True

    @admin.display(description="Текст вопроса", ordering="text")
    def short_text(self, question: Question) -> str:
        return f"{question.text[:settings.admin_preview_text]}"

    @admin.action(description="Опубликовать выбранные вопросы")
    def set_public(self, request: HttpRequest, queryset: QuerySet) -> None:
        count: int = queryset.update(status=Question.ModerationStatus.PUBLIC)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Отклонить публикацию выбранных вопросов")
    def set_declined(self, request: HttpRequest, queryset: QuerySet) -> None:
        count: int = queryset.update(status=Question.ModerationStatus.DECLINED)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created")
    list_display_links = ("name",)
    list_filter = ["name", "created"]
    list_per_page = settings.admin_elements_per_page
    fields = ["name", "slug"]
    readonly_fields = ["slug"]
    search_fields = ["name"]
    ordering = ["-created"]
    save_on_top = True
