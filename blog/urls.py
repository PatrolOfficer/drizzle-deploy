from django.urls import path, include
from . import views
from .views import (PostListView, 
                    PostDetailView, 
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView,
                    LatestPostView,
                    )
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),  #looks for <app>/<model>_<viewtype>.html
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('ckeditor/',include('ckeditor_uploader.urls')),

    path('tag/<slug:tag_slug>/',views.home, name='post_tag'),

    path('search/', views.home, name='search'),

    path('latest/', LatestPostView.as_view(), name='latest-post'),
    path('announcements/', views.announcements, name='blog-announcements'),
    path('about/', views.about, name='blog-about'),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)