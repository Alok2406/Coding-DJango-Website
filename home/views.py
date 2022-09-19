from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from home.models import Contact
from blog.models import Cpost
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    # code to show top_post on home page of code_smash
    top_post =Cpost.objects.all().order_by('-views').values()[0:3]
    context={'top_post':top_post}
    return render(request,'home/home.html',context)
    #return HttpResponse("we are at home")


def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        print(name,email,phone,desc)
        if len(name)<2 or len(email)<4 or len(phone)<10 or len(desc)<10:
            messages.error(request, ' please check your deatils')
        else:
            contact=Contact(name=name, email=email, phone=phone , desc=desc)
            contact.save()
            messages.success(request, ' form submited succesfully')
        
    return render(request,'home/contact.html')
    #return HttpResponse("contact home")

def about(request):
    return render(request,'home/about.html')
    #return HttpResponse("about us")


def search(request):
    query=request.GET['query']
    if len(query)>70:
        #allPosts=[] #this line is usable with len() function
        allPosts=Cpost.objects.none()

    else:
        allPostsTitle =Cpost.objects.filter(title__icontains=query)
        allPostsContent =Cpost.objects.filter(content__icontains=query)
        allPosts=allPostsTitle.union(allPostsContent)
    
    if allPosts.count()==0:
        #below len function line is usable with allPosts=[] 
        #if len(allPosts)==0: 
        messages.warning(request, "please check input")
    
    params={'allPosts':allPosts,'query':query}
    return render(request,'home/search.html',params)



#Authenticating API
#Sign Up Handaling
def handleSignup(request):
    if request.method =='POST':
        #Get the post parameter
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        #checks for blank field input
        
        #Username must be under 10 charecter long
        if len(username)>10:
            messages.error(request,"Username must be under 10 charecters")
            return redirect('home')
        
        #only letter and number allowed in Username
        if not username.isalnum():
            messages.error(request,"only letter and number allowed in Username")
            return redirect('home')    
        
        # both Password and confirm password entry mactch each other
        if pass1 != pass2:
            messages.error(request,"Password entry not mactch")
            return redirect('home')
        
        #Createuser
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request,"Your Account Has Been Created Succesfully")
        return redirect('home')
       
    else:
        return HttpResponse('404-Error Occured')


#log in & logout Handaling
def handlelogin(request):
    if request.method == 'POST':
        
        loginuser =request.POST['loginuser']
        loginpass =request.POST['loginpass']
        user=authenticate(username=loginuser,password=loginpass)
        if user is not None:
            login(request, user)
            messages.success(request,"Successfully Login")
            return redirect('home')
        else:
             return HttpResponse('404-Error Occured')   

def handlelogout(request):
    #if request.method=='POST':
    logout(request)
    messages.success(request,"Successfully Logout")
    return redirect('home')
    
      
    
