from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blogpost,Blogcomment,Contactus
from django.contrib import messages
from blog.templatetags import get_dict
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
# create your views here
# def index(request):
#     return HttpResponse("Index blog")
def index(request):
    allblogs=[]
    test=Blogpost.objects.all()
    # print(test)
    catblogs=Blogpost.objects.values('category','post_id')
    cats={post['category'] for post in catblogs}
    for cat in cats:
        cat1=Blogpost.objects.filter(category=cat)
        # n=len(cat1)
        allblogs.append(cat1)
    # print(allblogs)
    params={'allblogs':allblogs}
    return render(request,'blog/index.html',params)

def search(request):
    newblog=[]
    if request.method=='POST':
        blog2=request.POST.get('search','')
        if len(blog2)>0:
            blog=Blogpost.objects.values('category')
            # print(blog)
            new2={item3['category'] for item3 in blog}
            # for new3 in new2:
            blog3=Blogpost.objects.filter(category=blog2)
            # print("This is blog3:",blog3)
            # product2=Product.objects.all()
            n=len(blog3)
            newblog.append(blog3)
            params2={'newblog':newblog,'blog2':blog2 }
            # print("this is product",product)
            # print("this is newprods",newprods)
            # print("this is product2",product2)
            if len(blog3)==0:
                return HttpResponse('Blog not found')
            else:
                return render(request,"blog/search.html",params2)

    allblogs=[]
    catprods=Blogpost.objects.values('category','post_id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Blogpost.objects.filter(category=cat)
        n=len(prod)
        allblogs.append(prod)
    # allProds=[[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
    params={'allblogs':allblogs }
    return render(request,"blog/index.html", params)           
def aboutus(request):
    return render(request,'blog/aboutus.html')
def signup(request):
    return render(request,'blog/signup.html')
def signup2(request):
    if request.method=='POST':
        first_name=request.POST.get('firstname','')
        last_name=request.POST.get('lastname','')
        username=request.POST.get('username','')
        email=request.POST.get('email','')
        password=request.POST.get('password','')
        user1=User.objects.values('username')
        # users1={user2['username'] for user2 in user1}
        # for users2 in users1:
        #     if username in users2:
        #         print('user already exists')
        # print(first_name,last_name,username,email,password)
        try:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.first_name=first_name
            user.last_name=last_name
            user.save()
            return render(request,'blog/signup.html')
        except Exception as e:
            false1={'false2':'false'}
            return render(request,'blog/signup.html',false1)
def login2(request):
    return render(request,'blog/login.html')
def login3(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        print(username,password)
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,'blog/login.html')
def logout2(request):
    logout(request)
    return render(request,'blog/login.html')
def postComment(request):
    if request.method=='POST':
        comment2=request.POST.get('comment')
        user=request.user
        postSno=request.POST.get("postSno")
        # print("Thi sis postSno:",postSno)
        post=Blogpost.objects.get(post_id=postSno)
        # print(post)
        parentsno=request.POST.get("parentsno")
       
        if parentsno=="":
            comment=Blogcomment(comment=comment2,user=user,post=post)
            comment.save()
            messages.success(request,"Your comment has been posted successfully")
        else:
            parent=Blogcomment.objects.get(sno=parentsno)
            comment=Blogcomment(comment=comment2,user=user,post=post,parent=parent)
            comment.save()
            messages.success(request,"Your reply has been posted successfully")
        # comment=Blogcomment(comment=comment2,user=user,post=post)
    return redirect(f"/blog/blogpost/{post.post_id}")

def blogpost(request,id):
    blog=Blogpost.objects.filter(post_id=id).first()
    comments=Blogcomment.objects.filter(post=blog,parent=None)
    replies=Blogcomment.objects.filter(post=blog).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    # print(replyDict)
    # print("this is a comment:",comments, "This is a reply:",replies)
    # print(request.user)
    context={'blog':blog,'comments':comments,'user':request.user,'replyDict':replyDict}
    return render(request,'blog/blogpost.html',context)
def contactus(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        message=request.POST.get('message','')
        contact=Contactus(name=name,email=email,phone=phone,message=message)
        contact.save()
        confirm=True
        return render(request,'blog/contact.html',{'confirm':confirm})
    return render(request,'blog/contact.html')