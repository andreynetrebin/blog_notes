from django.utils.text import slugify


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