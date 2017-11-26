from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def set_color(request):
	if "fav_color" in request.GET:
		#create an HttpResponse object...
		response=HttpResponse("your favorite color is now %S"%request.GET["fav_color",'none'])
		#and set a cookie on the response
		return response
	else:
		return HttpResponse("you didn't give a favorite color")
		
def show_color(request):
	if "fav_color" in request.COOKIES:
		return HttpResponse("your favorite color is %s"%request.COOKIES['fav_color'])
	else:
		return HttpResponse("you don't have a favorite color.")