from django.contrib import admin

from articles.models import Article
from config.config import settings
from core.mixins import AdminMixin


@admin.register(Article)
class ArticleAdmin(AdminMixin, admin.ModelAdmin):
    list_display = ("user", "short_text", "status", "created")
    list_display_links = ("user", "short_text")
    list_editable = ("status",)
    search_fields = ["text", "user"]
    field = ["user", "created", "status", "slug", "text"]
    readonly_fields = ["slug"]
    ordering = ["-created"]
    list_filter = ["status", "created"]
    list_per_page = settings.admin_elements_per_page
    save_on_top = True

    @admin.display(description="Текст статьи", ordering="text")
    def short_text(self, model: Article, method_name: str = "text") -> str:
        return super().short_text(model, method_name)
