from django.shortcuts import render, redirect
from .models import Order, OrderItem, Product
from .forms import ProductForm, OrderForm
from django.contrib import messages
from django.views.generic import ListView, View, CreateView
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def index(request):
    product = Product.objects.all
    context = {'product': product}
    return render(request, 'welcome.html', context)


def createOrder(request):
    form = OrderForm()
    name = "User"
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            template = render_to_string('email.html', {'name': name, 'form': form})
            email = EmailMessage(
                'Order Confirmation',
                template,
                settings.EMAIL_HOST_USER,
                ['faizanmehdi69@gmail.com', 'rimshaurooj56@gmail.com'],
            )
            email.fail_silently = False
            email.send()
            print("Email sent")
            return redirect('welcome')
    context = {'form': form}
    return render(request, 'order.html', context)


def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        # print('Printing Post ', request.POST)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
            return redirect('welcome')
    context = {'form': form}
    return render(request, 'ProductForm.html', context)


def createpdf(request, pk):
    p = Product.objects.get(id=pk)
    template_path = 'pdfview.html'
    context = {'p': p}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Product Report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def updateProduct(request, pk):
    product = Product.objects.get(id=pk)

    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
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


def multi_click(request):
    return render(request, 'multiclick.html')


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
    order = OrderForm()
    if request.method == 'POST':
        # print('Printing Post ', request.POST)
        product = ProductForm(request.POST)
        order = OrderForm(request.POST)
        if product.is_valid() and order.is_valid():
            prod = product.save()
            order = order.save(commit=False)
            order.product = prod
            order.save()
            messages.success(request, 'Form submission successful')
            return redirect('welcome')
    context = {'pform': product, 'oform': order}
    return render(request, 'MultipleForm.html', context)


def template(request):
    return render(request, 'ajaxview.html')


def ajaxcall(request):
    return render(request, 'ajaxview.html')


def ajax_posting(request):
    if request.method == 'POST':
        print("here")
        name = request.POST.get('name')  # getting data from first_name input

        price = request.POST.get('price')  # getting data from last_name input
        quantity = request.POST.get('quantity')
        status = request.POST.get('status')
        productImg = request.POST.get('image')
        print(name, price, quantity, status)
        # if name and price and quantity and status:#cheking if first_name and last_name have value
        # print('Values are obtained')
        # price = int(price)
        # quantity = int(quantity)
        # print(price, quantity)

        # obj = Product.objects.create(
        #     name=name,
        #     price=price,
        #     quantity=quantity,
        #     status=status,
        # )
        # response = {
        #     'msg': 'Your form has been submitted successfully'  # response message
        # }
        #
        # user = {'name': obj.name, 'price': obj.price, 'quantity': obj.qunatity}

        data = {

        }

        return JsonResponse(data)  # return response as JSON

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
