from django.shortcuts import render


def sellers(request):

    return render(request,'sellers/sellers.html',locals())


