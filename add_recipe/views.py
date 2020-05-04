from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaultfilters import upper
from django.urls import reverse

from .models import Recipes
from cart.models import Cart
from cart.models import Checkout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.core.files.storage import FileSystemStorage

final_bill=0

# Create your views here.
@login_required
def addrecipe(request):
    return render(request, 'addrecipe.html')

@login_required
def add_submitted_recipe(request):

    if request.method=='POST':
        recipe_name = request.POST['recipe']
        image = request.POST['image']
        cuisine = request.POST['service']
        type = request.POST['type-product']
        range1 = request.POST['from-value']
        range2 = request.POST['to-value']
        ingredients = request.POST['Ingredients']
        recipe = request.POST['Recipe']
        note = request.POST['message']

        query = Recipes(recipe_name=recipe_name, image=image, cuisine=cuisine, type=type,
                                        range1=range1,range2=range2,ingredients=ingredients,recipe=recipe,note=note)
        query.save()
        return viewrecipe(request)

    else:
        return redirect('/')

@login_required
def viewrecipe(request):
    allitems=Recipes.objects.all()
    all_cart_items = Cart.objects.values('recipe_name').filter(cust_name=request.user.first_name)
    print(all_cart_items)
    cart_sent=[]
    for i in all_cart_items:
        cart_sent.append(i['recipe_name'])
    return render(request,'show_recipe.html',{'items':allitems,'cart_items': cart_sent})


@login_required
def add_cart(request,recipe_name):
    recipe_name = recipe_name
    current_user = request.user.first_name
    image_name = Recipes.objects.values('image').get(recipe_name=recipe_name)
    image_name=image_name['image']
    quantity = 1
    price_name = Recipes.objects.values('range2').get(recipe_name=recipe_name)
    price_name=price_name['range2']
    final_price=price_name*quantity

    cart_obj = Cart(cust_name=current_user, image=image_name, recipe_name=recipe_name, price=price_name, quantity=quantity,final_price=final_price,ticked=True)
    cart_obj.save()

    return viewrecipe(request)

@login_required
def view_cart(request):
    all_cart_items = Cart.objects.filter(cust_name=request.user.first_name)
    all_items = Cart.objects.filter(cust_name=request.user.first_name).values()
    sum1 = 0
    for i in all_items:
        sum1 = sum1 + i['quantity'] * i['price']
    res=(5*sum1)/100+sum1
    return render(request, 'cart.html', {'cart_items': all_cart_items,'res1':sum1,'res2':res})


@login_required
def delfrm_cart(request,recipe_name):
    Cart.objects.filter(recipe_name=recipe_name).delete()
    all_cart_items = Cart.objects.filter(cust_name=request.user.first_name)
    all_items = Cart.objects.filter(cust_name=request.user.first_name).values()
    sum1 = 0
    for i in all_items:
        sum1 = sum1 + i['quantity'] * i['price']
    res = (5 * sum1) / 100 + sum1
    return render(request, 'cart.html', {'cart_items': all_cart_items,'res1':sum1,'res2':res})


def filtering(request,type):
    allitems = Recipes.objects.filter(type=type)
    return render(request, 'show_recipe.html', {'items': allitems})


def viewpage(request,recipe_name):
    all_items = Recipes.objects.filter(recipe_name=recipe_name)
    all_cart_items = Cart.objects.values('recipe_name').filter(cust_name=request.user.first_name)
    print(all_cart_items)
    cart_sent = []
    for i in all_cart_items:
        cart_sent.append(i['recipe_name'])
    return render(request, 'view_page.html', {'items': all_items,'cart_items': cart_sent})


def checkout(request):
    all_cart_items = Cart.objects.filter(cust_name=request.user.first_name).values()
    sum1=0
    for i in all_cart_items:
        sum1 = sum1 + i['quantity'] * i['price']
    res = (5 * sum1) / 100 + sum1
    return render(request, 'checkout_address.html',{'units': all_cart_items, 'res':res})

def sub_quantity(request,recipe_name):
    random = Cart.objects.values('quantity').get(recipe_name=recipe_name)
    random_price = Cart.objects.values('price').get(recipe_name=recipe_name)
    a=0
    if random['quantity']>1:
        a = int(random['quantity']) - 1
    else:
        a= int(random['quantity'])
    Cart.objects.filter(recipe_name=recipe_name).update(quantity=a)
    final_price = random_price['price'] * a
    Cart.objects.filter(recipe_name=recipe_name).update(final_price=final_price)
    return view_cart(request)

def add_quantity(request,recipe_name):
    random=Cart.objects.values('quantity').get(recipe_name=recipe_name)
    random_price = Cart.objects.values('price').get(recipe_name=recipe_name)
    a=int(random['quantity'])+1
    final_price = random_price['price'] * a
    Cart.objects.filter(recipe_name=recipe_name).update(quantity=a)
    Cart.objects.filter(recipe_name=recipe_name).update(final_price=final_price)
    return view_cart(request)

def add_checkout_details(request):
    if request.method=='POST':
        name=request.POST['name']
        lastname=request.POST['lastname']
        email=request.POST['email']
        address=request.POST['address']
        address2=request.POST['address2']
        city=request.POST['city']
        state=request.POST['state']
        zip=request.POST['zip']
        user_id=request.user.id

        all_cart_items = Cart.objects.filter(cust_name=request.user.first_name).values()
        sum1 = 0
        for i in all_cart_items:
            sum1 = sum1 + i['quantity'] * i['price']
        res = (5 * sum1) / 100 + sum1

        amount=res

        check_obj=Checkout(name=name,lastname=lastname,email=email,address=address,address2=address2,city=city,state=state,zip=zip,userid=user_id,Amount=amount)
        check_obj.save()

        return render(request, 'creditcard2.html')
def payment(request):
    return render(request, 'thankyou.html')
def search(request):
    if request.method == 'POST':
        recipe_name = request.POST['recipe_name']
        all_items = Recipes.objects.filter(recipe_name=recipe_name)
        return render(request, 'view_page.html', {'items': all_items})
    else:
        return render(request, 'searchresult.html')

