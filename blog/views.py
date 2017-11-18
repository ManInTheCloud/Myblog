from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from blog.models import Article
from datetime import datetime
from django.http import Http404

# Create your views here.
def Test(request):
    return render(request,'blog/test.html',{'current_time':datetime.now()})

def home(request):
    post_list=Article.objects.all() #get all article objects
    return render_to_response('blog/home.html',{'post_list':post_list})

def Detail(request,id):
    try:
        post=Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render_to_response('blog/post.html',{'post':post})
