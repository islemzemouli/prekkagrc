from django.shortcuts import render, get_object_or_404
from .models import Article
from django.core.paginator import Paginator

# Liste des articles


def liste_articles(request):
    # Get only published articles
    articles = Article.objects.filter(publie=True).order_by('-date_creation')

    # Pagination: 5 articles per page
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    articles_page = paginator.get_page(page)

    # Get distinct categories for sidebar
    categories = Article.objects.values_list('categorie', flat=True).distinct()

    context = {
        'articles': articles_page,
        'categories': categories,
    }
    return render(request, 'blog/liste_articles.html', context)


# Détail d'un article
def detail_article(request, slug):
    # Get the requested article
    article = get_object_or_404(Article, slug=slug, publie=True)

    # Get other articles for sidebar (exclude current article)
    other_articles = Article.objects.filter(
        publie=True).exclude(id=article.id)[:5]

    # Get distinct categories for sidebar
    categories = Article.objects.values_list('categorie', flat=True).distinct()

    context = {
        'article': article,
        'other_articles': other_articles,
        'categories': categories,
    }
    return render(request, 'blog/detail_article.html', context)


# Liste des articles par catégorie
def articles_by_categorie(request, categorie):
    # Filter articles by category
    articles = Article.objects.filter(
        publie=True, categorie=categorie).order_by('-date_creation')

    # Pagination: 5 articles per page
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    articles_page = paginator.get_page(page)

    # Get distinct categories for sidebar
    categories = Article.objects.values_list('categorie', flat=True).distinct()

    context = {
        'articles': articles_page,
        'categories': categories,
        'current_category': categorie
    }
    return render(request, 'blog/liste_articles.html', context)
