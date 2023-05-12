from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    # if now.month == 1 and now.date == 1:
    #     return HttpResponse("It's New Year!!")
    # else:
    #     return HttpResponse("No, It's not New Year :/")

    return render(request, "newyear/index.html",{
        "newyear": now.month == 1 and now.date == 1,
    })