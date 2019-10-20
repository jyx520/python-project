from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render_to_response, redirect
from django.core.exceptions import PermissionDenied


# def index(request):
#     url = reverse('article_detail', args=(2020,))
#     url2 = reverse('auth:index')
#     print(url2)
#     return HttpResponse('我是首页' + url)
#
#
def article(request, year):
    # raise PermissionDenied  #页面返回 403 Forbidden
    return HttpResponse('article:' + year)

def index(request):
    return render_to_response("index.html ")

def index_one(request):
    '''  重定向 '''
    # return HttpResponseRedirect('/index2/')
    url = reverse('index_two')
    return redirect(url)
    # return redirect('/index2/')
    # return HttpResponse('index_one')

def page_500(request):
    ''' 重写500响应页面 '''
    return HttpResponse('服务器正忙......')


def page_404(request):
    ''' 重写404响应页面 '''
    return HttpResponse('资源已丢失。。。。。')


def index_two(request):
    '''  触发一个异常产生500 '''
    raise ValueError
    return HttpResponse('index_two')


def print_request(request):
    print(request)
    # print(request.META["REMOTE_ADDR"])
    print('----------------------')
    print(dir(request))
    return HttpResponse(str(dir(request)) + '\r\n' + str(request.META["REMOTE_ADDR"]))

