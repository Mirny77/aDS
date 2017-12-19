from django.shortcuts import render



def home(request):
    



    return render(request, 'goods/home.html', locals())