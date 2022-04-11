"""drf_vue_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.views import serve

from rest_framework.routers import DefaultRouter
from drf_vue_blog.views import dashboard
from article import views
from comment.views import CommentViewSet

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.generic.base import RedirectView


from user_info.views import UserViewSet
from service import views as service_views

router = DefaultRouter()
router.register(r'article', views.ArticleViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'tag', views.TagViewSet)
router.register(r'avatar', views.AvatarViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'user', UserViewSet)
router.register(r'service',service_views.ServiceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # 可视化接口
    path('api-auth/', include('rest_framework.urls')),
    # drf 默认路由器自动注册
    path('api/', include(router.urls)),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # 这里可以配置网页收藏夹的图标
    # path('favicon.ico', serve, {'path': '/admin/img/favicon.ico'}),
    path('favicon.ico',RedirectView.as_view(url='https://avatars2.githubusercontent.com/u/13655483?s=60&v=4')),
    path('admin/dashboard/', dashboard, name='dashboard'),

    # article
    # path('api/article/', include('article.urls', namespace='article')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)