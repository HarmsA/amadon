from django.shortcuts import render, redirect
from .models import Store

# Create your views here.
def index(request):
    if 'user_id' not in request.session:
        return redirect('/users/login')
    context ={
        "merchandise": Store.objects.all()
    }

    return render(request, 'store/index.html', context)


def checkout(request, total, id):
    pass

def calc(request):
    # print(request.POST)
    # print(Store.objects.get(id=request.POST['product_id']))
    total = Store.objects.calculate(request.POST)
    return redirect('/store/index/')
