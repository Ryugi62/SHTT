from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProductImage
import os

def add_product(request):
    if request.method == 'POST':
        new_product = Product.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            price=request.POST.get('price'),
            stock=request.POST.get('stock')
        )
        for file in request.FILES.getlist('images'):
            ProductImage.objects.create(product=new_product, image=file)
        return redirect('product_list')
    return render(request, 'add_product.html')


def product_list(request):
    return render(request, 'product_list.html', {'products': Product.objects.all()})


def delete_image_file(image):
    if os.path.isfile(image.image.path):
        os.remove(image.image.path)


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    for image in product.images.all():
        delete_image_file(image)
    product.delete()
    return redirect('product_list')


def delete_image(request, image_id):
    image = get_object_or_404(ProductImage, id=image_id)
    delete_image_file(image)
    image.delete()
    return redirect('edit_product', product_id=image.product.id)


def process_image_deletion(request, product):
    images_deleted = False
    for key, value in request.POST.items():
        if key.startswith("delete_image_") and value == "on":
            image_id = key.split("_")[-1]
            image = get_object_or_404(ProductImage, id=image_id)
            delete_image_file(image)
            image.delete()
            images_deleted = True
    return images_deleted


def update_product_images(request, product):
    for key in request.FILES:
        if key.startswith("update_image_"):
            image_id = key.split("_")[-1]
            image = get_object_or_404(ProductImage, id=image_id)
            image.image = request.FILES[key]
            image.save()


def add_new_images(request, product):
    for file in request.FILES.getlist('images'):
        ProductImage.objects.create(product=product, image=file)


def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        product.name = request.POST.get("name")
        product.description = request.POST.get("description")
        product.price = request.POST.get("price")
        product.stock = request.POST.get("stock")
        product.save()

        images_deleted = process_image_deletion(request, product)
        update_product_images(request, product)
        add_new_images(request, product)

        return redirect('edit_product', product_id=product.id) if images_deleted else redirect("product_list")
    return render(request, "edit_product.html", {"product": product})
