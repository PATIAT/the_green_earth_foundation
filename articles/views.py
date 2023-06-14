from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/article_detail.html', {'article': article})


def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles:article_list')
    else:
        form = ArticleForm()
    return render(request, 'articles/article_form.html', {'form': form})


def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/article_form.html', {'form': form})


def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:article_list')
    return render(request, 'articles/article_confirm_delete.html', {'article': article})
