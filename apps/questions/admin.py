from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from config.config import settings
from core.mixins import AdminMixin
from questions.models import Category, Question


@admin.register(Question)
class QuestionAdmin(AdminMixin, admin.ModelAdmin):
    list_display = ("title", "short_text", "level", "status", "created")
    list_display_links = ("title", "short_text")
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
    def short_text(self, model: Question, method_name: str = "text") -> str:
        return super().short_text(model, method_name)

    @admin.action(description="Опубликовать выбранные вопросы")
    def set_public(self, request: HttpRequest, queryset: QuerySet) -> None:
        super().set_public(request, queryset)

    @admin.action(description="Отклонить публикацию выбранных вопросов")
    def set_declined(self, request: HttpRequest, queryset: QuerySet) -> None:
        super().set_declined(request, queryset)


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
