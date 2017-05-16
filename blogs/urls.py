from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^amp/(?P<pk>\d+)$', views.AmpView.as_view(), name='amp'),
    url(r'^category/$', views.CategoryView.as_view(), name='category'),
    
    url(r'^user/me$', views.MyArticleView.as_view(), name='my_article'),
    url(r'^user/(?P<user>\w+)$', views.UserArticleView.as_view(), name='user_article'),
    url(r'^setting/$', views.SettingView.as_view(), name='setting'),
    url(r'^information_change/$', views.information_change, name='information_change'),

    url(r'^article/(?P<pk>\d+)$', views.ArticleView.as_view(), name='detail'),
    url(r'^search', views.SearchView.as_view(), name='search'),
    url(r'^feed/(?P<user>\w+)$', views.UserFeed(), name='feed'),

    url(r'^create/$', views.CreateView.as_view(), name='create'),
    url(r'^edit/(?P<pk>\d+)$', views.EditView.as_view(), name='editview'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^comment/$', views.comment, name='comment'),


    url(r'^login', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
]