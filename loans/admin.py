from django.contrib import admin

# Register your models here.

from .models import Loan, Reservation


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):

    list_display = (
        "book",
        "user",
        "loan_date",
        "due_date",
        "return_date",
        "status",
        "fine_amount",
    )

    list_filter = ("status", "loan_date", "due_date")

    search_fields = (
        "book__title",
        "user__username",
        "user__first_name",
        "user__last_name",
    )


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        "book",
        "user",
        "reserved_at",
        "status",
    )

    list_filter = ("status", "reserved_at")

    search_fields = (
        "book__title",
        "user__username",
    )
