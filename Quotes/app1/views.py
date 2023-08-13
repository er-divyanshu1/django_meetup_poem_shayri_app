from django.shortcuts import redirect, render
from app1.models import Category, Post,Reader

# Create your views here.
def index (request):
    categorys =Category.objects.all()
    posts =Post.objects.all()
    data={
        'categorys' : categorys,
        'post' : posts
    }
    return render(request,"index.html",data)

def category (request,url):
    
    categorys =Category.objects.all()
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)


    return render (request,"category.html",{'cat':cat, 'posts':posts,'categorys' : categorys,})

def about_us (request):
    return render (request,"about_us.html")


def term_condition (request):
    return render (request,"term_condition.html")


def contact_us (request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        reader = Reader(name=name, email=email, masssage=message)
        reader.save()
        return redirect('index')
        print(name,email,message)
    return render (request,"contact_us.html")

