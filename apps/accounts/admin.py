from django.contrib import admin

from accounts.models import Review, User
from config.config import settings
from core.mixins import AdminMixin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "is_superuser", "last_login", "created")
    list_display_links = ("email",)
    list_editable = ("is_superuser",)
    search_fields = ["email", "username"]

    field = ["email", "username", "is_superuser", "last_login", "created"]
    exclude = ["password", "first_name", "last_name"]

    readonly_fields = ["email"]
    ordering = ["is_superuser", "-last_login"]
    list_filter = ["is_superuser", "last_login", "created"]
    list_per_page = settings.admin_elements_per_page
    save_on_top = True


@admin.register(Review)
class ReviewAdmin(AdminMixin, admin.ModelAdmin):
    list_display = ("user", "short_text", "status", "created")
    list_display_links = ("user", "short_text")
    list_editable = ("status",)
    search_fields = ["text", "user"]
    field = ["user", "created", "status", "number_of_interview_sessions", "text"]
    ordering = ["-created"]
    list_filter = ["status", "created"]
    list_per_page = settings.admin_elements_per_page
    save_on_top = True

    @admin.display(description="Текст отзыва", ordering="text")
    def short_text(self, model: Review, method_name: str = "text") -> str:
        return super().short_text(model, method_name)
