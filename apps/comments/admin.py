from django.contrib import admin

from comments.models import Comment
from config.config import settings
from core.mixins import AdminMixin


@admin.register(Comment)
class CommentAdmin(AdminMixin, admin.ModelAdmin):
    list_display = ("user", "short_text", "created")
    list_display_links = ("user", "short_text")
    search_fields = ["text", "user"]
    field = ["user", "created", "text"]
    ordering = ["-created"]
    list_per_page = settings.admin_elements_per_page
    save_on_top = True

    @admin.display(description="Текст комментария", ordering="text")
    def short_text(self, model: Comment, method_name: str = "text") -> str:
        return super().short_text(model, method_name)
