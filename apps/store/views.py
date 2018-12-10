from django.shortcuts import render, redirect
from django.contrib import messages
from apps.users.models import User

from .models import Store

# Create your views here.
def index(request):
    # if 'user_id' not in request.session:
    #     return redirect('/users/login')
    # if 'sub_total' not in request.session:
    #     request.session['sub_total'] = 0
    # if 'item_id_list' not in request.session:
    #     request.session['item_id_list'] = []
    # context ={
    #     "merchandise": Store.objects.all(),
    #     'sub_total': request.session['sub_total'],
    #     'item_id_list': request.session['item_id_list'],
    # }

    return render(request, 'store/index.html')


def checkout(request):

    user = User.objects.get(id=request.session['user_id'])
    store_item = Store.objects.get(id=request.session['product_id'])
    context = {
        'name':user.f_name.capitalize(),
        'cost':request.session['single_order_price'],
        'total':request.session['sub_total']
    }

    return render(request, 'store/checkout.html', context)

def calc(request):
    if 'user_id' not in request.session:
        return redirect('/users/login')
    if 'sub_total' not in request.session:
        request.session['sub_total'] = 0

    cost = float(Store.objects.calculate(request.POST))
    subtotal = float(request.session['sub_total'])
    subtotal += cost

    request.session['single_order_price'] = cost
    request.session['product_id'] = request.POST['product_id']
    request.session['sub_total'] = subtotal

    """Save the order to the db and link it to the users profile"""
    # Store.objects.

    return redirect('store:checkout')
