from django.shortcuts import render , HttpResponse


def main_view(request):
    return HttpResponse("Hello, world.")
# Create your views here.


def html_view(request):
    return render(request,'main.html')