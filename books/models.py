from django.db import models

class Book(models.Model):
    title = models.CharField("عنوان کتاب", max_length=200)
    author = models.CharField("نویسنده", max_length=160)
    isbn = models.CharField("شابک", max_length=20, blank=True)
    category = models.CharField("دسته‌بندی", max_length=100, blank=True)
    published_year = models.PositiveIntegerField("سال انتشار", null=True, blank=True)
    total_copies = models.PositiveIntegerField("تعداد کل نسخه‌ها", default=1)
    available_copies = models.PositiveIntegerField("نسخه‌های موجود", default=1)
    description = models.TextField("توضیحات", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب‌ها"

    def __str__(self):
        return f"{self.title} — {self.author}"
