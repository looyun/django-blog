from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^category/$', views.CategoryView.as_view(), name='category'),
    url(r'^article/(?P<pk>\d+)$', views.ArticleView.as_view(), name='detail'),
    url(r'^create/$', views.CreateView.as_view(), name='create'),
    url(r'^edit/(?P<pk>\d+)$', views.EditView.as_view(), name='editview'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^search', views.SearchView.as_view(), name='search'),
]