from django.contrib import admin

from companies.models import Company
from config.config import settings


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created")
    list_display_links = ("name",)
    list_editable = ("slug",)
    search_fields = ["name"]
    ordering = ["-created"]
    fields = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    list_per_page = settings.admin_elements_per_page
    save_on_top = True
