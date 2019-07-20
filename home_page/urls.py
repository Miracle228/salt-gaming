"""salt_gaming URL Configurations
The `uratterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-basd views
    1. t:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    NewsListView,
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import  views as user_views
urlpatterns = [
     # path(r'jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
     path('news/', NewsListView.as_view(), name='news'),
     path('', PostListView.as_view(), name='home'),
     path('post/<int:pk>/', PostDetailView, name='post-detail'),
     path('post/new/', PostCreateView.as_view(), name='post-create'),
     path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
     path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
     path('register/',user_views.register, name='register' ),
     path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
     path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
     path('profile/',user_views.profile, name='profile' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
