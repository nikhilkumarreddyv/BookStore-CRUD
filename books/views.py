from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    if request.method=="POST":
        data=request.POST
        book_name=data.get("book_name")
        author_name=data.get("author_name")
        book_year=data.get("book_year")
        book_image=request.FILES.get("book_image")
        Book.objects.create(
            book_name=book_name,
            author_name=author_name,
            book_year=book_year,
            book_image=book_image
        )
        return redirect('/')
    
    queryset=Book.objects.all()
    

    if request.GET.get('search'):
        queryset=queryset.filter(book_name__icontains=request.GET.get('search'))
    
    context={'books':queryset}
    return render(request,'books/index.html',context)

def update_book(request,id):
    queryset=Book.objects.get(id=id)

    if request.method=='POST':
        data=request.POST
        book_name=data.get("book_name")
        author_name=data.get("author_name")
        book_year=data.get("book_year")
        book_image=request.FILES.get("book_image")

        queryset.book_name=book_name
        queryset.author_name=author_name
        queryset.book_year=book_year
        if book_image:
            queryset.book_image=book_image
        queryset.save()
        return redirect('/')

    context={'books':queryset}
    return render(request,'books/update.html',context)

def delete_book(request,id):
    queryset=Book.objects.get(id=id)
    queryset.delete()
    return redirect('/')