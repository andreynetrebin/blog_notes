from django.urls import path
from . import views
from . views import (
	CategoryListView,
	ItemsByCategoryView,
	ItemDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	SearchResultsView,
    CategoryCreateView,
	)


app_name = 'blog'

urlpatterns=[
	path('', CategoryListView.as_view() , name='category-list'),
    path('<str:slug>/', ItemsByCategoryView.as_view() , name='items-by-category'),
    path('item/<str:slug>/', ItemDetailView.as_view() , name='item-detail'),
	path('posts/create/', PostCreateView.as_view(), name='posts_create'),
    path('item/<str:slug>/update/', PostUpdateView.as_view(), name='posts_update'),
    path('item/<str:slug>/delete/', PostDeleteView.as_view(), name='posts_delete'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
	path('categories/create/', CategoryCreateView.as_view(), name='categories_create'),




]