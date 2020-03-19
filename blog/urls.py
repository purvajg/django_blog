from django.urls import path, include
from .import views
from .views import PostDetailView,PostListView
from django.contrib.auth import views as auth_views

urlpatterns = [

    # path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # When the user visits our site then he is directly given the login/signup
    # option rather than showing him the blogs directly

    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # adding variables into route. variable here is id of the blog or pk
    path('about/', views.about, name='blog-about'),
]
