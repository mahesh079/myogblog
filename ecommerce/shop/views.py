from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders,orderupdate
from math import ceil
import json
import re
# create your views here
def index(request):
    # products= Product.objects.all()
    # n=len(products)
    # nSlides = n // 4 + ceil((n / 4) - (n // 4))
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod,range(1,nSlides),nSlides])
    # allProds=[[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
    params={'allProds':allProds }
    return render(request,"shop/index2.html", params)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        message=request.POST.get('message','')
        contact=Contact(name=name,email=email,phone=phone,message=message)
        contact.save()
        confirm=True
        return render(request,'shop/contact.html',{'confirm':confirm})
    return render(request,'shop/contact.html')
def tracker(request):
    status=[]
    date=[]
    if request.method=="POST":
        orderid=request.POST.get('orderid','')
        email=request.POST.get('email','')
        order=Orders.objects.filter(order_id=orderid)
        if len(order)>0:
            update=orderupdate.objects.filter(orderid=orderid)
            # print(update)
            status=[]
            date=[]
            for item in update:
                 status.append(item.status)
                 date.append(item.timestamp) 
 
        params={'status':status,'date':date}
        return render(request,'shop/tracker.html',{'params':params})
    return render(request,'shop/tracker.html')
def search(request):
    product=Product.objects.values('category')
    newprods=[]
    product2={}
    if request.method=='POST':
        item2=request.POST.get('search','')
        if len(item2)>0:
            newprods=[]
            product=Product.objects.values('category')
            # print(product)
            new2={item3['category'] for item3 in product}
            # for new3 in new2:
            product2=Product.objects.filter(category=item2)
            # product2=Product.objects.all()
            n=len(product2)
            nSlides2 = n // 4 + ceil((n / 4) - (n // 4))
            newprods.append([product2,range(1,nSlides2),nSlides2])
            params2={'newprods':newprods,'item2':item2 }
            # print("this is product",product)
            # print("this is newprods",newprods)
            # print("this is product2",product2)
            if len(product2)==0:
                return HttpResponse('Product not found')
            else:
                return render(request,"shop/search.html",params2)

    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod,range(1,nSlides),nSlides])
    # allProds=[[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
    params={'allProds':allProds }
    return render(request,"shop/index2.html", params)
def productview(request,id):
    # fetch the product using id
    product=Product.objects.filter(id=id)
    # product=Product.objects.all()
    # print(product)
    return render(request,'shop/prodview.html',{'product':product[0]})
def checkout(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        state=request.POST.get('state','')
        city=request.POST.get('city','')
        pincode=request.POST.get('pincode','')
        address=request.POST.get('address','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        orders=Orders(name=name,state=state,city=city,pincode=pincode,address=address,email=email,phone=phone)
        orders.save()
        update=orderupdate(orderid=orders.order_id,status="The order has been placed")
        update.save()
        thank=True
        id=orders.order_id
        return render(request,'shop/checkout.html',{'thank':thank,'id':id})
    return render(request,'shop/checkout.html')