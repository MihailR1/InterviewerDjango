from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User, Review

admin.site.register(User, UserAdmin)
admin.site.register(Review)
