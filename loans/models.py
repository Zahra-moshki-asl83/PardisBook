from django.db import models

# Create your models here.

from decimal import Decimal

from django.conf import settings
from django.utils import timezone
from django.core.validators import MinValueValidator


class Loan(models.Model):

    class Status(models.TextChoices):
        ACTIVE = "active", "در حال امانت"
        RETURNED = "returned", "بازگردانده شده"
        CANCELLED = "cancelled", "لغو شده"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="loans",
        verbose_name="عضو کتابخانه"
    )

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.PROTECT,
        related_name="loans",
        verbose_name="کتاب"
    )

    loan_date = models.DateField(
        default=timezone.localdate,
        verbose_name="تاریخ امانت"
    )

    due_date = models.DateField(
        verbose_name="تاریخ بازگشت"
    )

    return_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="تاریخ تحویل واقعی"
    )

    status = models.CharField(
        max_length=12,
        choices=Status.choices,
        default=Status.ACTIVE,
        verbose_name="وضعیت امانت"
    )

    fine_amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=Decimal("0.00"),
        validators=[MinValueValidator(Decimal("0.00"))],
        verbose_name="مبلغ جریمه"
    )

    notes = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "امانت کتاب"
        verbose_name_plural = "امانت‌های کتاب"
        ordering = ["-loan_date"]

    def __str__(self):
        return f"{self.book.title} - {self.user.username}"

    @property
    def is_overdue(self):
        return (
            self.status == self.Status.ACTIVE
            and self.due_date < timezone.localdate()
        )


class Reservation(models.Model):

    class Status(models.TextChoices):
        PENDING = "pending", "در انتظار"
        READY = "ready", "آماده تحویل"
        CANCELLED = "cancelled", "لغو شده"
        EXPIRED = "expired", "منقضی شده"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="reservations",
        verbose_name="عضو کتابخانه"
    )

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.PROTECT,
        related_name="reservations",
        verbose_name="کتاب"
    )

    reserved_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="تاریخ رزرو"
    )

    status = models.CharField(
        max_length=12,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name="وضعیت رزرو"
    )

    class Meta:
        verbose_name = "رزرو کتاب"
        verbose_name_plural = "رزروهای کتاب"
        ordering = ["-reserved_at"]

    def __str__(self):
        return f"{self.book.title} - {self.user.username}"
