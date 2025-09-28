# urls.py dans l'application blog
from django.urls import path
from . import views

app_name = 'blog'  # namespace pour l'app

urlpatterns = [
    # page liste des articles
    path('', views.liste_articles, name='liste_articles'),
    path('<slug:slug>/', views.detail_article,
         name='detail_article'),  # page détail article
    path('categorie/<str:categorie>/', views.articles_by_categorie,
         name='articles_by_categorie'),

]
