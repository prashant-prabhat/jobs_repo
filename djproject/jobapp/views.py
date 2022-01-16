from django.shortcuts import render
from jobapp.models import *
from django.http import HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.

def index(request):
    return render(request,'testapp/index1.html')

def hydjobs1(request):
    jobs_list=hydjobs.objects.order_by('-date')
    paginator=Paginator(jobs_list,25)
    page_number=request.GET.get('page')
    try:
        jobs_list=paginator.page(page_number)
    except PageNotAnInteger:
        jobs_list=paginator.page(1)
    except EmptyPage:
        jobs_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/hydjobs.html',{'jobs_list':jobs_list})

def bangalore_jobs_view(request):
    s= '<h1>Bangalore jobs information you can get from here </h1>'
    return HttpResponse(s)

def patna_jobs_view(request):
        s= '<h1>patna jobs information you can get from here & get it soon </h1>'
        return HttpResponse(s)
