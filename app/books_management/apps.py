from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BooksManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books_management'
    verbose_name = _('books_management')
