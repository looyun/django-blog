from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<shortcode>[\w-]+)/$', views.URLRedirectView.as_view()),
    url(r'^',views.Index),
    url(r'^shorten/$',views.get_shorturl)
]
