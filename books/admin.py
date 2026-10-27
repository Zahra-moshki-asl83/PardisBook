from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "available_copies", "total_copies")
    search_fields = ("title", "author", "category", "isbn")
    list_filter = ("category",)
