#从 django.urls 导入了 path 函数
#从当前目录下导入了 views 模块。
from django.urls import path
from . import views

app_name = 'blog'
#把网址和处理函数的关系写在了 urlpatterns 列表(有序集合)里
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('archives/<int:year>/<int:month>/', views.ArchiveView.as_view(), name='archive'),
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('tags/<int:pk>/', views.TagView.as_view(), name='tag'),
    path('search/', views.search, name='search'),
]