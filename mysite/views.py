from django.shortcuts import render
#Create your views here

def Homepage(request):
    return render(request,'index.html',{})

def TestPage(request):
    return render(request,'test.html',{})

def ThanksPage(request):
    return render(request,'thanks.html',{})
