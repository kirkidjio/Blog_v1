from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<int:article_id>', views.article_show, name='article_url'),
    path('login', views.authorization, name='authorization'),
    path('logout', views.logout, name='logout'),
    path('addComment/<int:article_id_post>', views.commentPublication, name='publication_comment'),
    path('registration', views.register, name='register'),
    path('account/<int:account_id>', views.account_show, name='account_show'),
]



