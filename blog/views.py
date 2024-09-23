from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostCreateForm, PostUpdateForm, CategoryCreateForm
from .models import Post, Category
from django.db.models import Q
from django.urls import reverse_lazy


class CategoryListView(generic.ListView):
    model = Category
    template_name = "index.html"
    context_object_name = 'categories'

    def get_queryset(self):

        if self.request.user.is_anonymous:
            queryset = None
        else:
            queryset = Category.objects.filter(author=self.request.user)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['items'] = Post.objects.all()
        return context


class ItemsByCategoryView(generic.ListView):
    ordering = 'id'
    paginate_by = 10
    template_name = 'items_by_category.html'
    context_object_name = 'posts'

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        self.categories = Category.objects.filter(author=self.request.user)
        queryset = Post.objects.filter(category=self.category)
        queryset = queryset.order_by(self.ordering)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['category'] = self.category
        context['categories'] = self.categories
        return context


class ItemDetailView(generic.DetailView):
    model = Post
    template_name = 'item_detail.html'


class PostCreateView(generic.CreateView):
    """
    Представление: создание материалов на сайте
    """
    model = Post
    template_name = 'posts_create.html'
    form_class = PostCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи на сайт'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
    """
    Представление: создание материалов на сайте
    """
    model = Category
    template_name = 'categories_create.html'
    form_class = CategoryCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление категории на сайт'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class PostUpdateView(generic.UpdateView):
    """
    Представление: обновления материала на сайте
    """
    model = Post
    template_name = 'posts_update.html'
    context_object_name = 'post'
    form_class = PostUpdateForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Обновление статьи: {self.object.title}'
        return context

    def form_valid(self, form):
        # form.instance.updater = self.request.user
        form.save()
        return super().form_valid(form)


class PostDeleteView(generic.DeleteView):
    """
    Представление: удаления материала
    """
    model = Post
    success_url = reverse_lazy('blog:category-list')
    context_object_name = 'post'
    template_name = 'posts_delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Удаление статьи: {self.object.title}'
        return context


class SearchResultsView(generic.ListView):
    model = Post
    context_object_name = "posts"
    ordering = 'id'
    paginate_by = 10
    template_name = 'search_results.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        print(query)
        return Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )

