import string
import random

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views import View,generic
from .models import ShortURL

# Create your views here.


def Index(request):
    return render(request,'shorturl/index.html')


class URLRedirectView(View):
    def get(self,request,shortcode=None,*args,**kwargs):
        qs=ShortURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count()!=1 and not qs.exists():
            raise Http404
        obj=qs.first()
        print(obj.url)
        return HttpResponseRedirect('http://'+obj.url)

def create_shortcode(url):
    chars=string.ascii_letters+string.digits
    shortcode=''.join(random.choice(chars) for _ in range(6))
    if ShortURL.objects.filter(shortcode=shortcode):
        return create_shortcode(request)
    return shortcode

def get_shorturl(request,**kwargs):
    url=request.POST['url']
    shortcode=create_shortcode(url)
    kwargs['url']='127.0.0.1/'+shortcode
    return render(request,'shorturl/index.html')
    




