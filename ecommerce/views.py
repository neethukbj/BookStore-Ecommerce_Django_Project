from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404,redirect
from store.models import * 
from django.conf import settings 
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.views.decorators.csrf import csrf_exempt
from math import ceil
from django.contrib import messages 

import razorpay

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))


def BASE(request):
    return render(request,'Main/base.html')

def HOME(request):
    product = Product.objects.all()
    categories = Categories.objects.all()
    collections = Collections.objects.all()

    ITEMID = request.GET.get('product')
    if ITEMID:
        product = Product.objects.filter(product=ITEMID)
    else:
        product = Product.objects.filter(status='Publish')



    context = {
        'product':product,
        'categories':categories,
        'collections':collections,

    }

    return render(request,'Main/index.html',context)#index.html

#def COLLECTIONS(request):
    product = Product.objects.all()
    categories = Categories.objects.all()
    collections = Collections.objects.all()

    ITEMID = request.GET.get('collections')
    if ITEMID:
        product = Product.objects.filter(collections=ITEMID)
    else:
        product = Product.objects.filter(status='Publish')



    context = {
        'product':product,
        'categories':categories,
        'collections':collections,

    }

    return render(request,'Main/collections.html',context)


def FICTION(request):
    product = Product.objects.all()
    categories = Categories.objects.all()
    CATID = request.GET.get('categories')
    if CATID:
        product = Product.objects.filter(categories=CATID,status='Publish')

    else:
        product = Product.objects.filter(status='Publish')

    context = {
        'product':product,
        'categories':categories,

    }
    return render(request,'Main/fiction.html',context)


def BIOGRAPHIES(request):
    product = Product.objects.all()
    categories = Categories.objects.all()
    CATID = request.GET.get('categories')
    if CATID:
        product = Product.objects.filter(categories=CATID,status='Publish')

    else:
        product = Product.objects.filter(status='Publish')

    context = {
        'product':product,
        'categories':categories,

    }
    return render(request,'Main/biographies.html',context)
    

def CHILDRENS(request):
    product = Product.objects.all()
    categories = Categories.objects.all()
    CATID = request.GET.get('categories')
    if CATID:
        product = Product.objects.filter(categories=CATID,status='Publish')

    else:
        product = Product.objects.filter(status='Publish')

    context = {
        'product':product,
        'categories':categories,

    }
    return render(request,'Main/childrens.html',context)

def THRILLER(request):
    product = Product.objects.all()
    categories = Categories.objects.all()
    CATID = request.GET.get('categories')
    if CATID:
        product = Product.objects.filter(categories=CATID,status='Publish')

    else:
        product = Product.objects.filter(status='Publish')

    context = {
        'product':product,
        'categories':categories,

    }
    return render(request,'Main/thriller.html',context)

def CLASSICS(request):
    product = Product.objects.all()
    categories = Categories.objects.all()
    CATID = request.GET.get('categories')
    if CATID:
        product = Product.objects.filter(categories=CATID,status='Publish')

    else:
        product = Product.objects.filter(status='Publish')

    context = {
        'product':product,
        'categories':categories,

    }
    return render(request,'Main/classics.html',context)

def SELFHELP(request):
    product = Product.objects.all()
    categories = Categories.objects.all()
    CATID = request.GET.get('categories')
    if CATID:
        product = Product.objects.filter(categories=CATID,status='Publish')

    else:
        product = Product.objects.filter(status='Publish')

    context = {
        'product':product,
        'categories':categories,

    }
    return render(request,'Main/selfhelp.html',context)

def ALLBOOKS(request):
    product = Product.objects.all()
    categories = Categories.objects.all()
    collections = Collections.objects.all()
    filter_price = Filter_Price.objects.all()
    images = Images.objects.all()



    CATID = request.GET.get('categories')
    PRICE_FILTER_ID = request.GET.get('filter_price')
    ATOZID = request.GET.get('ATOZ')
    ZTOAID = request.GET.get('ZTOA') 
    PRICE_LOWTOHIGH=request.GET.get('PRICE_LOWTOHIGH')
    PRICE_HIGHTOLOW=request.GET.get('PRICE_HIGHTOLOW')
    NEWNESS_ID=request.GET.get('NEWNESS')



    if CATID:
        product = Product.objects.filter(categories=CATID,status='Publish')
    elif PRICE_FILTER_ID:
        product = Product.objects.filter(filter_price=PRICE_FILTER_ID,status='Publish')
    elif ATOZID:
        product = Product.objects.filter(status='Publish').order_by('name')
    elif ZTOAID:
        product = Product.objects.filter(status='Publish').order_by('-name')
    elif PRICE_LOWTOHIGH:
        product = Product.objects.filter(status='Publish').order_by('price')
    elif PRICE_HIGHTOLOW:
        product = Product.objects.filter(status='Publish').order_by('-price')
    elif NEWNESS_ID:
        product = Product.objects.filter(status='Publish',condition='New').order_by('-id')

    else:
        product = Product.objects.filter(status='Publish')

    context = {
        'product':product,
        'images':images,
        'categories':categories,
        'collections':collections,
        'filter_price':filter_price,

    }
    return render(request,'Main/allbooks.html',context)

def BOOK_DETAILS(request,id) :
    product = Product.objects.filter(id=id).first()
    images = Images.objects.filter(id=id).first()
    categories = Categories.objects.all()
    collections = Collections.objects.all()
    
    ITEMID = request.GET.get('collections')
    if ITEMID:
        prod = Product.objects.filter(collections=ITEMID)
    else:
        prod = Product.objects.filter(status='Publish')



    context = {
        'product':product,
        'prod':prod,
        'images':images,
        'categories':categories,
        'collections':collections,

    }

    
    return render(request,'Main/singlebook.html',context)

def QUICK_VIEW(request):
    product = Product.objects.filter(id=id).first()
    images = Images.objects.filter(id=id).first()
    categories = Categories.objects.all()
    collections = Collections.objects.all()
    
    ITEMID = request.GET.get('collections')
    if ITEMID:
        prod = Product.objects.filter(collections=ITEMID)
    else:
        prod = Product.objects.filter(status='Publish')



    context = {
        'product':product,
        'prod':prod,
        'images':images,
        'categories':categories,
        'collections':collections,

    }

    
    return render(request,'Main/collections.html',context)
    

def CONTACT_PAGE(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact_us(
            email=email,
            message=message,
        )
        #contact.save()
        #return redirect('collections')
        message = message
        email_from = settings.EMAIL_HOST_USER
        try:
            send_mail(message,email_from,['neethukbj@gmail.com'])
            contact.save()
            return redirect('collections')
        except:
            contact.save()
            return redirect('contact')
    
        

    return render(request,'Main/contact.html')



def HANDLESIGNUP(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')


        customer = User.objects.create_user(username,email,pass1)
        customer = customer.save()

        return redirect('collections')

    return render(request,'Registration/auth.html')

def HANDLELOGIN(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('collections')
        else:
            return redirect('login')

    return render(request,'Registration/auth.html')

def HANDLELOGOUT(request):

    logout(request)

    return redirect('collections')




@login_required(login_url="/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("collections")


@login_required(login_url="/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_detail(request):
    return render(request, 'Cart/cart_details.html')


def CHECK_OUT(request):
    amount_str = request.POST.get('amount')
    amount_float = float(amount_str)
    amount = int(amount_float)
    
    payment = client.order.create({
        "amount": amount*100, 
        "currency": "INR",
        "payment_capture":"1"
        
     })
    order_id = payment['id']
    context = {
        'order_id':order_id,
        'payment':payment,
    }
    return render(request,'Cart/checkout.html',context)

def REVIEW(request):
    return render(request,'Cart/review.html')

def PLACE_ORDER(request):
    
    if request.method == 'POST':
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(id=uid)
        cart = request.session.get('cart')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        country = request.POST.get('country')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        total_amount = request.POST.get('total_amount')


        
        order_id = request.POST.get('order_id')
        payment = request.POST.get('payment')

        context ={
            'order_id':order_id,
        }

        order = Order(
            user = user,
            firstname = firstname,
            lastname=lastname,
            country =country,
            city=city,
            address = address,
            state = state,
            postcode = postcode,
            phone = phone,
            email = email,
            payment_id = order_id,
            total_amount = total_amount,
    
        )
        order.save()

        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']
            total = a * b

            item = OrderItem(
                user = user,
                order = order,
                product = cart[i]['name'],
                image = cart[i]['image'],
                quantity = cart[i]['quantity'],
                price = cart[i]['price'],
                total = total,

            )
            item.save()
          



        return render(request,'Cart/placeorder.html',context)
    

@csrf_exempt
def SUCCESS(request):
    if request.method == 'POST':
        a = request.POST
        order_id =""
        for key,val in a.items():
            if key =='razorpay_order_id':
                order_id = val
                break
        user = Order.objects.filter(payment_id = order_id).first()
        user.paid = True
        user.save()
        request.session['cart'] ={}
    return render(request,'Cart/thank-you.html')


def YOUR_ORDER(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(id=uid)
    order = OrderItem.objects.filter(user=user)
    context ={
        'order':order
    }
    print(order)
    return render(request,'Main/your_order.html')

def AUTH(request):
    return render(request,'Main/login.html')

def ABOUT(request):
    return render(request,'Main/about.html')

def BLOG(request):
    return render(request,'Main/blog.html')

def COLLECTIONS(request):
    
    allProds =[]
    colprods = Product.objects.values('collections','id')
    cols = {item['collections'] for item in colprods}
    for col in cols:
        prod  = Product.objects.filter(collections=col)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nSlides),nSlides])




    context = {
        'allProds':allProds,
    

    }

    return render(request,'Main/collections.html',context)

def NEW(request):
    return render(request,'Main/blog.html')

def ADDTOCART(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Cart.objects.filter(user=request.user.id,product_id=prod_id)):
                    return JsonResponse({'status':"Product already in cart"})
                else:
                    prod_qty = int(request.POST.get('product_qty'))
                    Cart.objects.create(user=request.user,product_id=prod_id,product_qty=prod_qty)
                    return JsonResponse({'status':"Product added successfully"})
            else:
                return JsonResponse({'status':"No such Product Found"})

        else:
            return JsonResponse({'status':"Login to Continue"})

    return




