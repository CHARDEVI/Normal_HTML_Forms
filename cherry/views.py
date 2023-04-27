from django.shortcuts import render

# Create your views here.
from cherry.models import *
from django.http import HttpResponse

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        tn=Topic.objects.get_or_create(topic_name=tn)[0]
        tn.save()
        return HttpResponse(f"{tn} data is inserted")
    return render(request,'insert_topic.html')
def insert_webpage(request):
    d={'topic':Topic.objects.all()}
    if request.method=='POST':
        tn=request.POST['topic']
        n=request.POST['name']
        em=request.POST['mail']
        url1=request.POST['url']
        TO=Topic.objects.get(topic_name=tn)

        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,email=em,url=url1)[0]
        WO.save()
        
        return HttpResponse(f'{n} data is inserted')

    return render(request,'insert_webpage.html',d)

def single_select(request):
    d={'topic':Topic.objects.all()}
    return render(request,'single_select.html',d)
def radio_webpage(request):
    d={'topic':Topic.objects.all()}
    return render(request,'radio_webpage.html',d)

def checkbox_webpage(request):
    d={'topic':Topic.objects.all()}
    return render(request,'checkbox_webpage.html',d)

def insert_access(request):
    d={'webpage':Webpage.objects.all()}
    if request.method=='POST':
        n=request.POST['name']
        a=request.POST['author']
        d=request.POST['date']
        WO=Webpage.objects.get(name=n)
        AO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
        AO.save()
        return HttpResponse('Access data is inserted')


    return render(request,'insert_access.html',d)


def acc_single_select(request):
    d={'webpage':Webpage.objects.all()}
    return render(request,'acc_single_select.html',d)
def acc_radio_webpage(request):
    d={'webpage':Webpage.objects.all()}
    return render(request,'acc_radio_webpage.html',d)

def acc_checkbox_webpage(request):
    d={'webpage':Webpage.objects.all()}
    return render(request,'acc_checkbox_webpage.html',d)