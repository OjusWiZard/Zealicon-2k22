from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    exclude = ["password"]
    list_display = ["username", "email", "first_name", "last_name", "contact_no"]
    search_fields = ["username", "email", "first_name", "last_name", "contact_no"]


admin.site.register(User, UserAdmin)
