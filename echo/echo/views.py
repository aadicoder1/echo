from django.shortcuts import render

def home(request):
    return render(request,'base.html')
def playlist(request):
    return render(request,'playlist.html')
def favorite(request):
    return render(request,'favorite.html')
def login(request):
    return render(request,'login.html')
def popular_artist(request):
    return render(request,'popularartist.html')

