from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.
'''we are directing django to the index.html page when it comes from the urls.py page of the blog'''
def index(request):
    myposts=Blogpost.objects.all()
    print(myposts)
    return render(request,'blog/index.html',{'myposts':myposts})
def blogpost(request,id):

    '''corresponding to the id present in the urls, we have to grab the blogpost associated  with that id'''
    post=Blogpost.objects.filter(post_id=id)[0]
    '''by writing 0 at the end, we are passing the object at zeroth position but not the whole list (this list consists of one item only
    because the ids are unique)'''
    print(post)
    return render(request,'blog/blogpost.html',{'post':post})
'''# if we write the retuen command as return render(request,'index.html'), then it gives an error because the index.HTML
 file is available inside the blog directory inside the templates directory.initially django is at the tempates
directory but we ahve to direct it into the blog directory available inside the templates directory
for that we  are adding blog/index.html.
correct command-return render(request,'blog/index.html')
FOR BETTER UNDERSTANDING SEE THE FILE NAME ITS WRITTEN AS
index.html-blog/templates/blog'''
