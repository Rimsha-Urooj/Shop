from django.shortcuts import render, redirect
from .models import Order, OrderItem, Product
from .forms import ProductForm, OrderForm
from django.contrib import messages
from django.views.generic import ListView, View
from django.http import JsonResponse


def setCookie(request):
    response = render(request, 'setCookie.html')
    response.set_cookie('demo-cookie', 'This cookie set from set Cookie page', max_age=5)
    return response


def setSession(request):
    response = render(request, 'setSession.html')
    return response


def index(request):
    product = Product.objects.all
    context = {'product': product}
    return render(request, 'welcome.html', context)


def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        # print('Printing Post ', request.POST)
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
            return redirect('welcome')
    context = {'form': form}
    return render(request, 'ProductForm.html', context)


def updateProduct(request, pk):
    product = Product.objects.get(id=pk)

    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Form submission successful')
            return redirect('welcome')
    context = {'form': form}
    return render(request, 'ProductForm.html', context)


def show_products(request, pk):
    product = Product.objects.all()
    print(product)
    context = {'product': product}
    return render(request, 'index.html', context)


def show_orders(request, pk):
    orders = Order.objects.get(id=pk)
    print(orders)
    prod = orders.product.quantity
    print("quantity= ", prod)
    item = orders.orderitem_set.all()
    print(item)
    for i in item:
        print(i.subtotal)
    context = {'orders': orders}
    return render(request, 'order.html', context)


def show_orderItems(request, pk):
    items = OrderItem.objects.get(id=pk)
    print(items)
    context = {'orderItem': items}
    return render(request, 'orderItem.html', context)


def MultipleForm(request):
    product = ProductForm()
    order = OrderForm
    if request.method == 'POST':
        # print('Printing Post ', request.POST)
        product = ProductForm(request.POST)
        order = OrderForm(request.POST)
        if product.is_valid() and order.is_valid():
            product.save()
            order.save()
            messages.success(request, 'Form submission successful')
            return redirect('welcome')
    context = {'pform': product, 'oform': order}
    return render(request, 'MultipleForm.html', context)


def template(request):
    return render(request, 'ajaxview.html')


def ajax_posting(request):
    if request.is_ajax():
        name = request.POST.get('first_name', None) # getting data from first_name input
        price = request.POST.get('price', None)# getting data from last_name input
        quantity = request.POST.get('quantity', None)
        status = request.POST.get('status', None)
        # if name and price and quantity and status:#cheking if first_name and last_name have value
        print('Values are obtained')
        price = int(price)
        quantity = int(quantity)
        print(price, quantity)

        obj = Product.objects.create(
            name=name,
            price=price,
            quantity=quantity,
            status=status,
        )

        user = {'name': obj.name, 'price': obj.price, 'quantity': obj.qunatity}

        data = {
            'user': user
        }
        response = {
                     'msg':'Your form has been submitted successfully' # response message
        }
        return JsonResponse(data, response) # return response as JSON


# class AjaxView(ListView):x
#     model = Product
#     template_name = 'ajaxview.html'
#     context_object_name = 'product'
#
#
# class CreateCrudUser(View):
#     def get(self, request):
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         quantity = request.POST.get('quantity')
#         status = request.POST.get('status')
#         image = request.POST.get('image')
#
#         prod = Product.objects.create(
#             name=name,
#             price=price,
#             quantity=quantity,
#             status=status,
#             productImg=image,
#         )
#
#         product = {'id': prod.id, 'name': prod.name, 'price': prod.price, 'quantity': prod.age, 'status': prod.status, 'productImg': prod.productImg }
#
#         data = {
#             'product': product
#         }
#         return JsonResponse(data)
#
# def AddProduct(request):
#     product = Product.objects.all()
#     data = {}
#     if request.POST.get('action') == 'POST':
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         quantity = request.POST.get('quantity')
#         status = request.POST.get('status')
#         image = request.POST.get('image')
#
#         data['name'] = name
#         data['price'] = price
#         data['quantity'] = quantity
#         data['status'] = status
#         data['image'] = image
#
#         Product.objects.create(
#             name=name,
#             price=price,
#             quantity=quantity,
#             status=status,
#             productImg=image,
#         )
#         return JsonResponse(data)
#     context = {'product': product}
#     return render(request, 'ajaxview.html', context)
