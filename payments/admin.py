from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "order_id",
        "amount_paid",
        "amount_due",
        "receipt",
        "status",
        "created_at",
    )


admin.site.register(Order, OrderAdmin)
