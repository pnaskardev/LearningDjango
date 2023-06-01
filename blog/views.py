from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        'author':'CoreyMS',
        'title':'Blog Post 1',
        'content':'First Post content',
        'date_posted':"June 1 2023"
    },
    {
        'author':'Priyanshu Naskar',
        'title':'Blog Post 2',
        'content':'Second Post content',
        'date_posted':"June 2 2023"
    }
]

def home(request):
    context={
        'posts':posts,
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html',{'title':'About'})
