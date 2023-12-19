from django.shortcuts import render

# Create your views here.


def TTExamDash(request):
    return render(request,'termTestExamDash.html')

def mainDash(request):
    return render(request,'main.html')

def genDash(request):
    return render(request,'generate.html')