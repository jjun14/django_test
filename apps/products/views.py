from django.shortcuts import render, redirect
from django.core import serializers
from apps.products.models import Product, Brand
def index(request):
  data = serializers.serialize("python", Product.objects.all())
  context = {
      "products": Product.objects.all().select_related('brand'),
      "brands": Brand.objects.all(),
      "data" : data,
  }
  return render(request, 'products/index.html', context)
def add(request):
  print request.POST
  if(request.method == "POST"):
    errors = []
    if not request.POST.get('brand', ''):
      errors.append('New product must have a brand')
    if not request.POST.get('product_name', ''):
      errors.append('New product must have a name')
    if len(request.POST['product_name']) < 8:
      errors.append('Product name should be at least 8 characters')
    if not request.POST.get('price', ''):
      errors.append('New  product must have a price')
    if request.POST['price'] and float(request.POST['price']) == 0:
      errors.append('New product price must be greater than $0')
    if not request.POST.get('description', ''):
      errors.append('New product must have a description')
    if len(errors) == 0:
      b = Brand.objects.get(id = request.POST['brand'])
      Product.objects.create(name=request.POST['product_name'],price=request.POST['price'],description=request.POST['description'],brand
        = b) 
    else:
      print "errors"
      request.session['errors'] = errors
      print request.session['errors']
    return redirect('index')
def delete(request, product_id):
  if request.method == "GET":
    print product_id
    p = Product.objects.get(id = product_id)
    p.delete()
  return redirect('index')
def edit(request, product_id):
  if request.method == 'GET':
    brands = Brand.objects.all()
    product = Product.objects.select_related('brand').get(id=product_id)
    context = {
        "product": product,
        "brands": brands,
    }
    return render(request,'products/product.html', context)
  else:
    return redirect('index')
def update(request):
  if request.method == 'POST':
    print request.POST
    p = Product.objects.filter(id = request.POST['product_id'])
    b = Brand.objects.get(id=request.POST['brand'])
    p.update(name = request.POST['product_name'], price = request.POST['price'],
        description=request.POST['description'], brand=b)
  return redirect('index')
