from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"/Users/fedhaalmutairi/Dev/taibahsite/taibahcommunity/taibahcommunitysite/index/templates/home.html")

