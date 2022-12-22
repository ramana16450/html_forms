from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
         tn=request.POST['topic']
         T=Topic.objects.get_or_create(topic_name=tn)[0]
         T.save()
         return HttpResponse('data inserted succesfully')
    return render(request,'insert_topic.html')

def insert_webpage(request):
     topics=Topic.objects.all()
     d={'topics':topics}
     if request.method=='POST':
          topic=request.POST['topic']
          na=request.POST['na']
          ur=request.POST['ur']
          T=Topic.objects.get_or_create(topic_name=topic)[0]
          T.save()
          W=webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
          W.save()
          return HttpResponse('webpage data is inserted successfully')
     return render(request,'insert_webpage.html',d)


      


def insert_accessrecords(request):
     topic=Topic.objects.all()
     d={'topic':topic}
     Webpage=webpage.objects.all()
     if request.method=='POST':
          topic=request.POST['topic']
          na=request.POST['na']
          ur=request.POST['ur']
          dt=request.POST['dt']
          T=Topic.objects.get_or_create(topic_name=topic)[0]
          T.save()
          W=webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
          W.save()
          A=Accessrecords.objects.get_or_create(name=W,date=dt)[0]
          A.save()
          return HttpResponse('Accessrecords are inserted succesfully')
     return render(request,'insert_accessrecords.html',d)

def insert_topic(request):
    if request.method=='POST':
        #tn=request.POST['topic']
        tn=request.POST.get('topic')
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('Topic is inseted successfully')

    return render(request,'insert_topic.html')

def insert_webpage(request):
    topics=Topic.objects.all()
    d={'topics':topics}

    if request.method=='POST':
        topic=request.POST['topic']
        na=request.POST['na']
        ur=request.POST['ur']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        return HttpResponse('Webpage is inserted se=uccessfully')
    return render(request,'insert_webpage.html',d)

def select_topic(request):
    topics=Topic.objects.all()
    d={'topics':topics}

    if request.method=='POST':
        tn=request.POST.getlist('topic')
        print(tn)
        webpages=webpage.objects.none()
        for i in tn:
            webpages=webpages|webpage.objects.filter(topic_name=i)
        data={'webpages':webpages}
        return render(request,'display_webpage.html',data)
    return render(request,'select_topic.html',d)

def checkbox(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'checkbox.html',d)
