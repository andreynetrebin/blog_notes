from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager


# creating model manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


# post model
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = RichTextUploadingField(verbose_name='Содержание')

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/')
    tags = models.ManyToManyField('Tag', blank=True)

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])


class PostFile(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d", verbose_name='Файл')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Статья')

    class Meta:
        verbose_name = 'Файл к статье'
        verbose_name_plural = 'Файлы к статье'


class Category(MPTTModel):
    title = models.CharField(max_length=150, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('post-by-category', args=[str(self.slug)])

    def __str__(self):
        return self.title
