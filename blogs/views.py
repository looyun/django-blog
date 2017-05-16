# _*_ coding:utf-8 _*_
import markdown
import datetime
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404

from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.views import generic
from django.db.models import Q

from .models import Article,Comment
from . import forms, models
#Feed
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator

# Create your views here.



class UserFeed(Feed):
    def title(self,obj):
        return obj.username+"'s article."

    def link(self,obj):
        return reverse('blogs:feed', args=[obj.username])

    def description(self,obj):
        return"Feeds for "+obj.username
    
    def get_object(self,request,user):
        return get_object_or_404(User,username=user)

    def items(self,obj):
        return Article.objects.filter(author=obj).order_by('-pub_date')[:]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return mark_safe(markdown.markdown(item.content, ['extra']))

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('blogs:detail', args=[item.pk])


class IndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.order_by('-edit_date')

    def get_context_data(self, **kwargs):
        kwargs['isHome'] = True
        kwargs['isLogin'] = isLogin(self.request)
        return super(IndexView, self).get_context_data(**kwargs)

class CategoryView(generic.ListView):
    template_name = 'blogs/category.html'
    context_object_name = 'articles'

    def get_queryset(self,**kwargs):
        kwargs['isCategory']=True
        return Article.objects.order_by('-pub_date')

    def get_context_data(self, **kwargs):
        kwargs['isCategory'] = True
        kwargs['isLogin'] = isLogin(self.request)
        return super(CategoryView, self).get_context_data(**kwargs)

@method_decorator(login_required, name='dispatch')
class SettingView(generic.DetailView):
    model = User
    template_name = 'blogs/setting.html'

    def get_context_data(self, **kwargs):
        kwargs['isLogin'] = isLogin(self.request)
        return super(SettingView, self).get_context_data(**kwargs)     
        
    def get_object(self):
        return self.request.user

@login_required
def information_change(request):
    user = User.objects.get(pk=request.POST['pk'])
    
    MyProfileForm = forms.ProfileForm(request.POST, request.FILES)

    if user == request.user:
        if request.POST.get("username"):
            user.username = request.POST.get("username")
        if request.POST.get("email"):
            user.email = request.POST.get("email")
        if request.FILES['avatar']:
            if MyProfileForm.is_valid():
                print request.POST
                print request.FILES
                print MyProfileForm

                user.myuser.avatar = MyProfileForm.cleaned_data['avatar']
            else:
                MyProfileForm = Profileform()
        user.save()
        return redirect("blogs:setting")
    else:
        return redirect("blogs:index")

class AmpView(generic.DetailView):
    model = Article
    template_name = 'blogs/amp.html'

    def get_context_data(self, **kwargs):
        kwargs['comments'] = self.object.comment_set.all()
        return super(AmpView, self).get_context_data(**kwargs)

class ArticleView(generic.DetailView):
    model = Article
    template_name = 'blogs/article.html'

    def get_context_data(self, **kwargs):
        kwargs['isLogin'] = isLogin(self.request)
        kwargs['comments'] = self.object.comment_set.all()
        article = self.object
        kwargs['isAuthor'] = isAuthor(self.request,article)
        article.views += 1
        article.save()
        return super(ArticleView, self).get_context_data(**kwargs)

@method_decorator(login_required, name='dispatch')
class MyArticleView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        kwargs['isLogin'] = isLogin(self.request)
        return super(MyArticleView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user).order_by('-edit_date')


class UserArticleView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        kwargs['isLogin'] = isLogin(self.request)
        return super(UserArticleView, self).get_context_data(**kwargs)
    
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs['user'])
        return Article.objects.filter(author=user).order_by('-edit_date')

@method_decorator(login_required, name='dispatch')
class CreateView(generic.CreateView):
    template_name = "blogs/create.html"
    model = models.Article
    form_class = forms.ArticleForm

    @csrf_exempt
    def form_valid(self, form):
        if isLogin(self.request):
            article = form.save(commit=False)
            article.author = self.request.user
            article.edit_date = datetime.datetime.now()
            article.save()
            return redirect("blogs:index")
        else:
            return redirect("blogs:login")

    def get_context_data(self, **kwargs):
        kwargs['isLogin'] = isLogin(self.request)
        return super(CreateView, self).get_context_data(**kwargs)

class SearchView(generic.ListView):
    template_name = 'blogs/search.html'
    context_object_name = 'articles'


    def get_context_data(self, **kwargs):
        kwargs['isLogin'] = isLogin(self.request)
        return super(SearchView, self).get_context_data(**kwargs)
    
    def get_queryset(self):
        keyword = self.request.GET.get('keyword')
        return Article.objects.filter(Q(title__contains=keyword)|Q(author__username__contains=keyword))

@method_decorator(login_required, name='dispatch')
class EditView(generic.DetailView):
    model = Article
    template_name = 'blogs/edit.html'

    def get_context_data(self, **kwargs):
        kwargs['isLogin'] = isLogin(self.request)
        return super(EditView, self).get_context_data(**kwargs)

@login_required
def edit(request):
    article = Article.objects.get(pk=request.POST['pk'])
    if isAuthor(request,article):
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.edit_date = datetime.datetime.now()
        article.save()
        return redirect("blogs:detail",request.POST['pk'])
    else:
        return redirect("blogs:login")

@login_required
def delete(request):
    article=Article.objects.get(pk=request.POST['pk'])
    if isAuthor(request,article):
        article.delete()
        return redirect("blogs:index")
    else:
        return redirect("blogs:login")


@login_required
def comment(request):
    article = Article.objects.get(pk=request.POST['pk'])
    article.reply_count+=1
    comment = Comment.objects.create(article=article,user=request.user,content=request.POST['content'])
    article.save()
    return redirect("blogs:detail",article.id)

def login(request):
    if request.method=='GET':
        return render(request,'blogs/login.html')
    else:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('blogs:index')
        else:
            return redirect('blogs:login')

def logout(request):
    auth.logout(request)
    return redirect('blogs:index')


def register(request):
    if request.method=='GET':
        return render(request,'blogs/register.html')
    else:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if not(username and email and password):
            return redirect('blogs:register')
        if User.objects.filter(username=username).exists():
            return redirect('blogs:login')
        else:
            user=User.objects.create_user(username,email,password)
            login(request)
            return redirect('blogs:index')
            
def isLogin(request):
    if request.user.is_authenticated():
        return True
    else:
        return False

def isAuthor(request,article):
    if request.user==article.author:
        return True
    else:
        return False
        

