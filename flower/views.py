from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.template import loader
from django.views.decorators.csrf import csrf_exempt 
from .models import Items, ItemDetails, Cart
from.form import CreateUserForm, LoginUserForm, ShippingAddressForm, PaymentForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Sum


@login_required(login_url='auth_login')
def checkout(request):
    template = loader.get_template('checkout.html')
    current_user = request.user.id
    cart = Cart.objects.filter(id_user=current_user)  # Fetch everything for current_user

    cart_details = []  # List to store all retrieved items

    for item in cart:
        item_detail = ItemDetails.objects.get(id=item.id_product)
        product_name = item_detail.itemsid.name  # To get product name from the related Items object
        total = cart.aggregate(Sum('total'))['total__sum'] if cart else 0
        cart_details.append({
            'cart_item': item,
            'product_name': product_name
        })

    context = {
        'cart_details': cart_details,
        'total':total
    }
    return HttpResponse(template.render(context=context))

def index(request): 
    template = loader.get_template('index.html') 
    return HttpResponse(template.render())

@login_required(login_url='auth_login')
def shop(request): 
    template = loader.get_template('shop.html') 
    flower = ItemDetails.objects.select_related('itemsid')
    print(flower.query)
    return HttpResponse(template.render({'flower':flower, 'request':request}))

@login_required(login_url='auth_login')
def productdetails(request, id): 
    template = loader.get_template('productdetails.html') 
    flower = ItemDetails.objects.select_related('itemsid').filter(id=id)
    context={
        'flower': flower,
        'request':request
    }
    print(flower.query)
    return HttpResponse(template.render(context))

@login_required(login_url='auth_login')
def shipping_address(request): 
    template = loader.get_template('shipping_address.html') 
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment')
        else:
            print(form.errors)
    else:
        form = ShippingAddressForm()
    return HttpResponse(template.render({'form': form}, request))

@login_required(login_url='auth_login')
def payment(request): 
    template = loader.get_template('payment.html') 
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PaymentForm()
    return HttpResponse(template.render({'form': form}, request))

@login_required(login_url='auth_login')
@csrf_exempt
def add_to_cart(request, id):
    currentuser=request.user
    discount=2
    status=False
    flower = ItemDetails.objects.select_related('itemsid').filter(id=id)
    count=0

    for item in flower:
        net=item.total-discount
        count=count+1
    cart=Cart(
        id_product=item.id,
        id_user=currentuser.id,
        price=item.price,
        qty=item.qty,
        tax=item.tax,
        image=item.image,
        total=item.total,
        discount=discount,
        net=net,
        status=status,
    )
            
    currentuser = request.user.id
    count=Cart.objects.filter(id_user=currentuser).count()
    cart.save()
    request.session['countcart']=count
    return redirect("/shop")

@csrf_exempt
def auth_login(request):
    template = loader.get_template('auth_login.html') 
    form=LoginUserForm()
    if request.method=="POST":
        form=LoginUserForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return render(request, 'index.html')
    context={'form':form}
    return render (request,'auth_login.html', context)

@csrf_exempt
def auth_register(request):
    template = loader.get_template('auth_register.html')
    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth_login')
    context={'registerform':form}
    return HttpResponse(template.render(context=context))

@csrf_exempt
def auth_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    
