# from django.urls import path
# from article import views
#
# app_name = 'article'
#
# urlpatterns = [
#     path('', views.ArticleList.as_view(), name='list'),
#     path('<int:pk>/', views.ArticleDetail.as_view(), name='detail'),
# ]

from django.contrib import admin
from django.urls import path
from .views import dashboard, dashboard_home

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard_home/', dashboard_home, name='dashboard_home'),
]
