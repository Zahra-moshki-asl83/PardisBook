
from django.db import models
from django.db.models import F, Q
from django.core.exceptions import ValidationError


class Book(models.Model):

    title = models.CharField(
        "عنوان کتاب",
        max_length=200
    )

    author = models.CharField(
        "نویسنده",
        max_length=160
    )

    publisher = models.CharField(
        "ناشر",
        max_length=150,
        blank=True
    )

    isbn = models.CharField(
        "شابک",
        max_length=20,
        blank=True
    )

    category = models.CharField(
        "دسته‌بندی",
        max_length=100,
        blank=True
    )

    published_year = models.PositiveIntegerField(
        "سال انتشار",
        null=True,
        blank=True
    )

    edition = models.CharField(
        "نوبت چاپ",
        max_length=50,
        blank=True
    )

    page_count = models.PositiveIntegerField(
        "تعداد صفحات",
        null=True,
        blank=True
    )

    language = models.CharField(
        "زبان کتاب",
        max_length=50,
        default="فارسی"
    )

    cover = models.ImageField(
        "تصویر جلد کتاب",
        upload_to="books/covers/",
        blank=True
    )

    shelf_location = models.CharField(
        "محل قرارگیری در کتابخانه",
        max_length=100,
        blank=True
    )

    total_copies = models.PositiveIntegerField(
        "تعداد کل نسخه‌ها",
        default=1
    )

    available_copies = models.PositiveIntegerField(
        "نسخه‌های موجود",
        default=1
    )

    description = models.TextField(
        "توضیحات",
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ["title"]

        verbose_name = "کتاب"

        verbose_name_plural = "کتاب‌ها"

        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["author"]),
            models.Index(fields=["category"]),
        ]

        constraints = [
            models.CheckConstraint(
                condition=Q(
                    available_copies__lte=F("total_copies")
                ),
                name="book_available_copies_lte_total"
            )
        ]

    def clean(self):

        super().clean()

        if self.available_copies > self.total_copies:

            raise ValidationError({
                "available_copies":
                "تعداد نسخه‌های موجود نمی‌تواند بیشتر از تعداد کل باشد."
            })

    def __str__(self):

        return f"{self.title} — {self.author}"
