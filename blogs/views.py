# _*_ coding:utf-8 _*_
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse

from .models import Article
from . import forms, models

# Create your views here.

# class IndexView(generic.ListView):


class IndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'articles'

    def get_queryset(self,**kwargs):
        kwargs['isHome']=True
        return Article.objects.order_by('-edit_date')


class CategoryView(generic.ListView):
    template_name = 'blogs/category.html'
    context_object_name = 'articles'

    def get_queryset(self,**kwargs):
        kwargs['isCategory']=True
        return Article.objects.order_by('-pub_date')


class ArticleView(generic.DetailView):
    model = Article
    template_name = 'blogs/article.html'


class CreateView(generic.CreateView):
    template_name = "blogs/create.html"
    model = models.Article
    form_class = forms.ArticleForm

    @csrf_exempt
    def form_valid(self, form):

        article = form.save(commit=False)
        article.author = self.request.user
        article.save()
        return redirect("/blogs/")


class SearchView(generic.ListView):
    template_name = 'blogs/search.html'
    context_object_name = 'articles'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword')
        return Article.objects.filter(title__contains=keyword)


class EditView(generic.DetailView):
    model = Article
    template_name = 'blogs/edit.html'

def edit(request):
    article = Article.objects.get(pk=request.POST['pk'])
    article.title = request.POST.get("title")
    article.content = request.POST.get("content")
    article.save()
    return redirect("/blogs/article/"+request.POST['pk'])

def delete(request):
    article=Article.objects.get(pk=request.POST['pk'])
    article.delete()
    return redirect("/blogs/")


def login(request):
    if request.method=='GET':
        return render(request,'blogs/login.html')
    else:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/blogs')
        else:
            return redirect('/blogs/login')

def register(request):
    if request.method=='GET':
        return render(request,'blogs/register.html')
    else:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            return redirect('/blogs/login')
        else:
            user=User.objects.create_user(username,email,password)
            login(request,user)
            return redirect('/blogs')



