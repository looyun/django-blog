from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<shortcode>[\w-]+)/$', views.URLRedirectView.as_view(),name='shortcode'),
    url(r'^$',views.get_shorturl,name='shorturl')
]
