from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from .utils import post_get_unique_slug, category_get_unique_slug
from ckeditor_uploader.fields import RichTextUploadingField

# post model
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField(max_length=250, blank=True, null=True)
    category = TreeForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = RichTextUploadingField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/',  default='featured_image/default.jpg',)
    # tags = models.ManyToManyField('Tag', blank=True)

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    # objects = models.Manager()  # The default manager.


    def save(self, *args, **kwargs):
        post_get_unique_slug(self)
        super(Post, self).save(*args, **kwargs)


    def get_absolute_url(self):
      kwargs = {
        'slug': self.slug
      }
      return reverse('blog:item-detail', kwargs=kwargs)



class PostFile(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d", verbose_name='Файл')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Статья')

    class Meta:
        verbose_name = 'Файл к статье'
        verbose_name_plural = 'Файлы к статье'


class Category(MPTTModel):
    title = models.CharField(max_length=150, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')
    slug = models.SlugField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_categorires')

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('blog:items-by-category', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        category_get_unique_slug(self)
        super(Category, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.title)
