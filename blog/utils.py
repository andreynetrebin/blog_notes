from pytils.translit import slugify
import os
from django.core.files.storage import FileSystemStorage
from blog_notes import settings
from urllib.parse import urljoin
from datetime import datetime


def post_process_slug(self, i):
    i += 1
    from .models import Post
    slug_filter = Post.objects.filter(slug__exact=self.slug)
    if len(slug_filter) == 1:
        if not slug_filter[0].pk == self.pk:
            self.slug = f"{slugify(self.title)}-{i}"
            post_process_slug(self, i)


def post_get_unique_slug(self):
    if not self.slug:
        self.slug = slugify(self.title)
        i = 1
        post_process_slug(self, i)


def category_process_slug(self, i):
    i += 1
    from .models import Category
    slug_filter = Category.objects.filter(slug__exact=self.slug)
    if len(slug_filter) == 1:
        if not slug_filter[0].pk == self.pk:
            self.slug = f"{slugify(self.title)}-{i}"
            category_process_slug(self, i)


def category_get_unique_slug(self):
    if not self.slug:
        self.slug = slugify(self.title)
        i = 1
        category_process_slug(self, i)


class CkeditorCustomStorage(FileSystemStorage):
    """
    Кастомное расположение для медиа файлов редактора
    """

    def get_folder_name(self):
        return datetime.now().strftime('%Y/%m/%d')


    def get_valid_name(self, name):
        return name



    def _save(self, name, content):
        folder_name = self.get_folder_name()
        name = os.path.join(folder_name, self.get_valid_name(name))
        return super()._save(name, content)


    location = os.path.join(settings.MEDIA_ROOT, 'uploads/')
    base_url = urljoin(settings.MEDIA_URL, 'uploads/')