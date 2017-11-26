from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def home(request):
	#request.session.set_test_cookie()	#to test if the cookie work
	return render_to_response("test/test.html")

def set_color(request):
	#if request.session.test_cookie_work():
	#	request.session.delete_test_cookie()
	if 'fav_color' in request.GET:
		request.session['fav_color']=request.GET['fav_color']
		return HttpResponse("session:your favorite color is %s"%request.session['fav_color'])
	else:
		HttpResponse("session:you don't give a favorite color")
	#else:
	#	return HttpResponse("Please enable cookie and try again.")
	'''
	#using cookie
	if "fav_color" in request.GET:
		#create an HttpResponse object...
		response=HttpResponse("cookie:your favorite color is now %s"%request.GET["fav_color"])
		#and set a cookie on the response
		response.set_cookie('fav_color',request.GET['fav_color'])
		return response
	else:
		return HttpResponse("cookie:you didn't give a favorite color")
	'''
		
def show_color(request):
	if 'fav_color' in request.session:
		fav_color=request.session['fav_color']
		del request.session['fav_color']
		return HttpResponse("session:your favorite color is %s"%fav_color)
	else:
		return HttpResponse("session:you don't give a favorite color")
	'''
	#using cookie
	if "fav_color" in request.COOKIES:
		return HttpResponse("cookie:your favorite color is %s"%request.COOKIES['fav_color'])
	else:
		return HttpResponse("cookie:you don't have a favorite color.")
	'''