from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Author(models.Model):
    full_name = models.CharField(_('full name'), max_length=255)

    class Meta:
        db_table = 'authors'
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

    def __str__(self):
        return self.full_name


class Book(models.Model):
    isbn_validator = RegexValidator(
        regex=r'^[0-9]{13}$',
        message='ISBN должен состоять из 13 цифр.'
    )
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    year = models.PositiveSmallIntegerField(_('Date of publication'), default=2023)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, validators=[isbn_validator])
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'books'
        ordering = ['-year']
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    @classmethod
    def create(cls, title, description, year, author_full_name, isbn):
        author, created = Author.objects.get_or_create(full_name=author_full_name)
        book = cls.objects.create(title=title, description=description, year=year, author=author, isbn=isbn)
        return book

    def __str__(self):
        return self.title
