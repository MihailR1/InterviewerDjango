from django.contrib import admin

from accounts.models import Review, User
from config.config import settings


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
class ReviewAdmin(admin.ModelAdmin):
    pass
