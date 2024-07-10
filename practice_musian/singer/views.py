from django.shortcuts import render,redirect
from .import forms
from . import models

# Create your views here.
def add_singer(request):
   
    if request.method=='POST':
         singer_form=forms.SingerForm(request.POST)
         if singer_form.is_valid():
            singer_form.save()
            return redirect('add_singer')
    
    else:
         singer_form=forms.SingerForm()


    return render(request,'add_singer.html',{'form':singer_form})

def edit_singer(request,id):
    singer=models.Singer.objects.get(pk=id)
    singer_form=forms.SingerForm(instance=singer)
    if request.method=='POST':
        singer_form=forms.SingerForm(request.POST,instance=singer)
        if singer_form.is_valid():
            singer_form.save()
           
    return render(request,'add_singer.html',{'form':singer_form})

def delete_singer(request,id):
     singer=models.Singer.objects.get(pk=id)
     singer.delete()
     return redirect('homepage')
            

