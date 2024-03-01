from django.contrib import admin

from companies.models import Company
from config.config import settings


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created")
    list_display_links = ("slug",)
    list_editable = ("name",)
    search_fields = ["name"]
    ordering = ["-created"]
    fields = ["name", "slug"]
    readonly_fields = ["slug"]
    list_per_page = settings.admin_elements_per_page
    save_on_top = True
