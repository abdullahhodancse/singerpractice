from django.shortcuts import render
from album.models import Singer

def home(request):
    data = Singer.objects.all()  
    print(data)
    return render(request, 'home.html', {'data': data})  
