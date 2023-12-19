from django.shortcuts import render

# Create your views here.


def fileUpload(request):
    return render(request,'upload.html')