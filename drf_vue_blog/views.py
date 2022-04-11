from django.contrib.auth.models import User
from django.shortcuts import render
from article.models import Article

def dashboard(request):
    user_count = User.objects.count()
    article_count = Article.objects.count()

    context = { 'user_count': user_count, 'task_count': article_count }
    return render(request, 'dashboard.html',context)