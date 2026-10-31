
from django.contrib import admin
from .models import MemberProfile


@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "membership_number",
        "phone_number",
        "joined_at",
        "is_active",
    )

    list_filter = ("is_active", "joined_at")

    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "membership_number",
        "phone_number",
    )
