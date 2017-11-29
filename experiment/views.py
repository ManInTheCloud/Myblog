from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.template import RequestContext
# Create your views here.
def home(request,template_name):
	#request.session.set_test_cookie()	#to test if the cookie work
	return render_to_response(template_name)

def my_view(request,month,day):
    pass

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

#############################################################################
def use_message(request):
	request.user.message_set.create(
		message='You got a new message'
	)
	return render_to_response('test/test.html',context_instance=RequestContext(request))

############################################################################
def method_splitter(request,*arg,**kwargs):
    get_view=kwargs.pop("GET",None)
    post_view=kwargs.pop("POST",None)
    if request.method=='GET' and get_view is not None:
        return get_view(request,*arg,**kwargs)
    elif request.method=='POST' and post_view is not None:
        return post_view(request,*arg,**kwargs)
    raise Http404
'''
def some_page_get(request,*arg,**kwargs):
    assert request.method=="GET","request.method is not GET"
    do_something_for_get()
    return render_to_response('page.html')

def some_page_post(request,*arg,**kwargs):
    assert request.method=="POST","request.method is not POST"
    do_something_for_post()
    return HttpResponseRedirect('/someurl/')
'''
###########################################################################
def requires_login(view):
    def real_view(request,*args,**kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/')
        return view(request,*args,**kwargs)
    return real_view()

#############################################################################
def custom_proc(request):
    '''
    A context processor that provides 'app','user',and 'ip_address'
    :param request:
    :return:
    '''
    return {
        'app':'My app',
        'user':request.user,
        'ip_address':request.META['REMOTE_ADDR']
    }

def view_1(request):
    #...
    return render_to_response(
        'template1.html',
        {'message':'I am view 1.'},
        context_instance=RequestContext(request,processors=[custom_proc])
    )