# blog/posts/views.py
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
posts = [
    {
        "id": 1,
        "title": "Let's explore Python",
        "content": "Python is an interpreted, high-level, general-purpose programming language. Widely used in web development, data science, and machine learning."
    },
    {
        "id": 2,
        "title": "Django for Web Development",
        "content": "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It follows the 'Don't Repeat Yourself' principle."
    },
    {
        "id": 3,
        "title": "Machine Learning Basics",
        "content": "Machine learning is a subset of artificial intelligence that enables computers to learn from data without explicit programming."
    },
    {
        "id": 4,
        "title": "REST APIs with Django Rest Framework",
        "content": "Django Rest Framework (DRF) is a powerful and flexible toolkit for building Web APIs in Django applications."
    },
    {
        "id": 5,
        "title": "Understanding Databases in Django",
        "content": "Django supports various databases like PostgreSQL, MySQL, and SQLite. The ORM allows easy interaction with the database using Python code."
    }
]

# posts=[]
def home(request):
    html=""
    for post in posts:
        html +=f'''
            <div> 
            <a href="/post/{post['id']}">
            <h1> {post['id']} - {post['title']} </h1> </a>
            <p1> {post['content'] } </p1>
            </div>
        '''
    username = "tanvir Hasan Abir"
    return render(request,'posts/home.html',{"posts":posts,"username" : username})

def post(request,id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True
            break
    if valid_id:
        return render(request,"posts/post.html",{"post_dict":post_dict })
    else : 
        return HttpResponseNotFound("Post is not found :(")

def google(request,id):
    # return HttpResponseRedirect("http://www.google.com")
    url = reverse("idcheck",args=[id])
    return HttpResponseRedirect(url)