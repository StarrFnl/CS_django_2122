from django.shortcuts import render, get_object_or_404

def order(request):
    return render(request, 'payment/order.html')

def cart(request):
    return render(request, 'payment/cart.html')

def wish(request):
    return render(request, 'payment/wish.html')

def complete(request):
    return render(request, 'payment/complete.html')

def error(request):
    return render(request, 'payment/error.html')
