from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Category
from .Forms import ProductForm

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("product_list")

    else:
        form = ProductForm()

    return render(request, "store/product_form.html", {
        "form": form,
    })


def update_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect("product_detail", id=product.id)

    else:
        form = ProductForm(instance=product)

    return render(request, "store/product_form.html", {
        "form": form,
        "product": product,
    })


def delete_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.delete()
        return redirect("product_list")

    return render(request, "store/product_confirm_delete.html", {
        "product": product,
    })


def home(request):
    return render(request, "store/home.html")


def product_list(request):
    products = Product.objects.all()

    search = request.GET.get("search")

    if search:
        products = products.filter(name__icontains=search)

    return render(request, "store/product_list.html", {
        "products": products,
    })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    return render(request, "store/product_detail.html", {
        "product": product,
    })


def category_products(request, id):
    category = get_object_or_404(Category, id=id)

    products = Product.objects.filter(category=category)

    return render(request, "store/category_products.html", {
        "category": category,
        "products": products,
    })