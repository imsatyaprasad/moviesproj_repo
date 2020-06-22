from django.shortcuts import render
from .forms import MovieForm
from .models import Movie
# Create your views here.
def index_view(request):
    return render(request,'index.html')

def addmovie(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('data transferred to DB')
        return index_view(request)
    return render(request,'ADD Movie.html',{'form':form})

def list_movies(request):
    movielist=Movie.objects.all()
    return render(request,'listmovie.html',{'movielist':movielist})
