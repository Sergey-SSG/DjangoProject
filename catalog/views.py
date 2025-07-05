from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from catalog.models import Product

from .forms import ProductForm


def home(request):
    product_list = Product.objects.order_by("-created_at")
    paginator = Paginator(product_list, 5)  # 5 товаров на страницу
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "catalog/home.html", {"page_obj": page_obj})


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message_text = request.POST.get("message")

        # Здесь можно добавить сохранение в базу или отправку письма
        print(f"[Контактная форма] Имя: {name}, Телефон: {phone}, Сообщение: {message_text}")

        # Добавляем сообщение об успешной отправке
        messages.success(request, f"Спасибо, {name}! Ваше сообщение получено.")

        # Можно вернуть ту же страницу, чтобы отобразилось сообщение
        return render(request, "catalog/contacts.html")

    return render(request, "catalog/contacts.html")


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "catalog/product_detail.html", {"product": product})


def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProductForm()
    return render(request, "catalog/product_add.html", {"form": form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('catalog:product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)

    return render(request, 'catalog/product_edit.html', {'form': form, 'product': product})