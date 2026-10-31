
from django.conf import settings
from django.db import models


class MemberProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="member_profile",
        verbose_name="حساب کاربری"
    )

    membership_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="شماره عضویت"
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True,
        verbose_name="شماره تماس"
    )

    address = models.TextField(
        blank=True,
        verbose_name="نشانی"
    )

    joined_at = models.DateField(
        auto_now_add=True,
        verbose_name="تاریخ عضویت"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="عضویت فعال"
    )

    class Meta:
        verbose_name = "پروفایل عضو"
        verbose_name_plural = "اعضای کتابخانه"
        ordering = ["-joined_at"]

    def __str__(self):
        return f"{self.user.username} - {self.membership_number}"
