from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movies
from .form import Newform


# Create your views here.
def data(request):
    movie = movies.objects.all()
    return render(request,'index.html',{'key':movie})
def main(request,uniq_id):
    page = movies.objects.get(id=uniq_id)
    return render(request,'main.html',{'pas':page})
def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        order = movies(name=name,desc=desc,year=year,img=img)
        order.save()
    return render(request,'insert.html')

def update(request,uid):
    movie = movies.objects.get(id=uid)
    form = Newform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'movie':movie,'form':form})

def delete(request,id):
    if request.method == 'POST':
        movie = movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')