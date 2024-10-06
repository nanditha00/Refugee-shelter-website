from django.shortcuts import render
from django.http import HttpResponse
from .models import Shelters
# Create your views here.

#gome route
def home(request):
    if request.method=="POST":
        x=request.POST
        loc=x.get("loc")
        data=Shelters.objects.filter(location=loc)
        context={"shell":data}
        return render(request,"home/home.html",context)
    data=Shelters.objects.all()
    context={"shell":data}
    return render(request,"home/home.html",context)

#disaster news route
def news(request):
    return render(request,"home/news.html")

#individual shelter page route
def  info(request,id):
    data=Shelters.objects.get(id=id)
    context={"s":data}
    return render(request,"home/shelterinfo.html",context)

#registered page route
def dec(request,id):
    data=Shelters.objects.get(id=id)
    data.current_size-=1
    data.save()
    diff = data.max_size - data.current_size    
    context={"info":data,"diff":diff}
    return render(request,"home/registered.html",context)

    
