from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

# creating model manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

# post model
class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body = RichTextUploadingField()
    # body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/')
    # tags = models.ManyToManyField('Tag', blank=True, )

    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.        
    tags = TaggableManager() 

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.slug])    

class PostFile(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


    objects = models.Manager()  # The default manager.        

# class Tag(models.Model):
#     name = models.CharField(max_length=250)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name    