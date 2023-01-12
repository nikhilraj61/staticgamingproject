from django.shortcuts import render,redirect
from .models import shop
from .forms import modelform
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    pr=shop.objects.all()
    return render(request,'index.html',{'pr':pr})


def detail(request,book_id):
    pr1=shop.objects.get(id=book_id)
    return render(request,'detail.html',{'product':pr1})

def add_product(request):
    if request.method == 'POST':
        name=request.POST['name']
        price=request.POST['price']
        desc=request.POST['desc']
        img=request.FILES['img']
        obj=shop(name=name,price=price,desc=desc,img=img)
        obj.save()
        print('PRODUCT added')
        return redirect('/')
    return render(request,'add_product.html')



def update(request,id):
    obj=shop.objects.get(id=id)
    form=modelform(request.POST or None ,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'obj':obj,'form':form})


def delete(request,id):
    if request.method=='POST':
        sos=shop.objects.get(id=id)
        sos.delete()
        return redirect('/')
    return render(request,'delete.html')