from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, models
from . import forms

# Create your views here.

def index(request):
    cards = Article.objects.order_by('-pub_date')[:5]
    context = {'cards':cards}

    return render(request, 'index.html', context)



def article_show(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = Article.objects.get(id=article_id).comment_set.order_by('-pub_date')
    return render(request, 'articles.html', {'article' : article, 'comments': comments})


def authorization(request):
    if request.method == "POST":
        user_name = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse(f'Something wrong with logining! {login} {password}')
    else:
        return HttpResponse('Something wrong with POST!')

def logout(request):
    pass

@login_required
def commentPublication(request, article_id_post):

    if request.method == "POST":
        form = forms.CommentForm(data={'comment' : request.POST['comment_text'],'author' : request.user, 'article':article_id_post})
        if form.is_valid():
            form.save()
            return redirect(f"/articles/{article_id_post}")
        else:

            return HttpResponse(f'Something wrong, POST: {form.errors}')


def register(request):
    if request.method == "POST":
        user = models.User.objects.create_user(request.POST['login'], password=request.POST['password'], email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])

        return redirect('/')
    else:
        return render(request, 'registration.html', {})


def account_show(request, account_id):
    user = User.objects.get(id=account_id)
    articless = user.article_set.order_by('-pub_date')
    commentss = user.comment_set.order_by('-pub_date')
    articles = articless[:3]
    comments = commentss[:3]
    articles_length = len(articless)
    comments_length = len(commentss)


    context = {'user': user, 'articles': articles, 'comments': comments, 'articles_length': articles_length, 'comments_length': comments_length}
    return render(request, 'showAccount.html', context)
