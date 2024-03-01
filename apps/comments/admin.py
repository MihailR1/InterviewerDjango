from django.contrib import admin

from comments.models import Comment
from config.config import settings


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "short_text", "created")
    list_display_links = ("user", "short_text")
    search_fields = ["text", "user"]
    field = ["user", "created", "text"]
    ordering = ["-created"]
    list_per_page = settings.admin_elements_per_page
    save_on_top = True

    @admin.display(description="Текст комментария", ordering="text")
    def short_text(self, comment: Comment) -> str:
        return f"{comment.text[:settings.admin_preview_text]}"
