from django.http import HttpResponse
from django.shortcuts import render,redirect
from blog.models import Cpost, BlogComment
from django.contrib import messages
from django.contrib.auth.models import User
from blog.templatetags import extras
# Create your views here.

def blogHome(request):
    allPosts=Cpost.objects.all()
    context={'allPosts' : allPosts}
    return render(request,'blog/bloghome.html',context)
    
def blogPost(request,slug):
    post=Cpost.objects.filter(slug=slug).first()
    post.views=post.views + 5
    post.save()
    comments=BlogComment.objects.filter(post=post,parent=None)
    replies=BlogComment.objects.filter(post=post).exclude(parent=None)
    replydict={}
    for reply in replies:
        if reply.parent.sno not in replydict.keys():
            replydict[reply.parent.sno]=[reply]
        else:
            replydict[reply.parent.sno].append(reply)
    print(replydict)            
    #print(comments,replies)
    print(request.user)
    context={'post':post,'comments':comments,'user':request.user,'replydict':replydict}
    
    return render(request,"blog/blogpost.html",context)
    

def postComment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        postSno=request.POST.get("postSno")
        post=Cpost.objects.get(sno=postSno)
        parentSno=request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request,"Your Comments has been Posted Succesfully")
        
        else:
            parent=BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment=comment,user=user,post=post,parent=parent)
        
            comment.save()
            messages.success(request,"Your reply has been Posted Succesfully")

        return redirect(f"/blog/{post.slug}")    
