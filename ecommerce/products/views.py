from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from cart.forms import CartAddProductForm
from django.db.models import Q, Count
from .models import*
# Create your views here.

def home(request):
    allcategory = Category.objects.all()
    allproducts = Product.objects.all()
    cart_product_form = CartAddProductForm()
    context = {
		'cart_product_form':cart_product_form,
        'allcategory':allcategory,
        'allproducts':allproducts,
	}
    return render(request,'pages/home.html',context)

def Categories(request,cat_id):
    allcategory = Category.objects.all()
    mycategory = Category.objects.get(id=cat_id)
    allproducts = Product.objects.all().filter(cat_id = cat_id )
    Pcounts = Product.objects.filter(cat_id=cat_id).count()
    allcounts=Product.objects.count()
    cart_product_form = CartAddProductForm()
    context={
        "allproducts":allproducts,
        "allcategory":allcategory,
        "mycategory":mycategory,
        "Pcounts":Pcounts,
        "allcounts":allcounts,
        'cart_product_form':cart_product_form,

    }
    return render(request,'pages/category.html',context)


# def Products(request,productid):
#     allcategory = Category.objects.all()
#     myproduct = Product.objects.get(id=productid)
#     return render(request,'pages/product.html',{"allcategory":allcategory,"myproduct":myproduct})

def descendingsort(request):
    allcategory = Category.objects.all()
    allproducts = Product.objects.all().order_by("-id")
    return render(request,'pages/descendingsort.html',{"allproducts":allproducts,"allcategory":allcategory})

def aescendingsort(request):
    allcategory = Category.objects.all()
    allproducts = Product.objects.all().order_by("id")
    return render(request,'pages/aescendingsort.html',{"allproducts":allproducts,"allcategory":allcategory})

def add_to_cart(request,pid):
    order_item=Product.objects.get(id=pid)
    allproducts = Product.objects.all().filter(id=pid)
    return render(request,'pages/cart.html',{"order_item":order_item,"allproducts":allproducts})

def product_detail(request,productid):
    allcategory = Category.objects.all()
    myproduct = Product.objects.get(id=productid)
    product = get_object_or_404(Product,id=productid)
    cart_product_form = CartAddProductForm()
    context = {
		'product':product,
		'cart_product_form':cart_product_form,
        'allcategory':allcategory,
        'myproduct':myproduct,
	}
    return render(request,'pages/product.html',context)
	

# def cart(request):
#     return render(request,'pages/cart.html')

# def add_cart(request, slug):
#     if request.user.is_authenticated:
#     item = get_object_or_404(Product,slug=slug)
#     order_item ,created = OrderItem.objects.get_or_create(
#         user=request.user,
#         item =item,
#     )
#     print(order_item)

#     order_qs = Cart.objects.filter(user=request.user, ordered=False)
#     if order_qs.exists():
#         order= order_qs[0]
#         # check if the order item is in the order
#         if order.products.filter(item__slug=item.slug).exists():
#             order_item.quantity+= 1
#             order_item.save()
#             print("1")
#         else:
#             order.products.add(order_item)
#     else:
#         order = Cart.objects.create(
#             user=request.user
#         )
#         order.products.add(order_item)
#         print("done")
#     return redirect("cart:home")
# else:
#     item = get_object_or_404(Product,slug=slug)
#     order_item ,created = OrderItem.objects.get_or_create(
#         user=None,
#         item =item,
#     )
#     print(order_item)

#     order_qs = Cart.objects.filter(user=None, ordered=False, session_key=request.session.session_key)
#     if order_qs.exists():
#         order= order_qs[0]
#         # check if the order item is in the order
#         if order.products.filter(item__slug=item.slug).exists():
#             order_item.quantity+= 1
#             order_item.save()
#             print("1")
#         else:
#             order.products.add(order_item)
#     else:
#         order = Cart.objects.create(
#             user=None, session_key=request.session.session_key
#         )
#         order.products.add(order_item)
#         print("done")
#     return redirect("cart:home")