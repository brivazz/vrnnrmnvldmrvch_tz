from django.contrib import admin
from .models import Book, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    search_fields = ('full_name', 'id')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'isbn', 'get_author')
    list_filter = ('year', 'author')
    search_fields = ('title', 'description')
    save_on_top = True
    save_as = True

    def get_author(self, obj):
        return obj.author.full_name

    get_author.short_description = 'Автор книги'


admin.site.site_title = 'Управление книгами'
admin.site.site_header = 'Управление книгами'
