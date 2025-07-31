from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .models import Product
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "page_obj"
    paginate_by = 5
    ordering = ["-created_at"]


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message_text = request.POST.get("message")
        print(f"[Контактная форма] Имя: {name}, Телефон: {phone}, Сообщение: {message_text}")
        messages.success(request, f"Спасибо, {name}! Ваше сообщение получено.")
        return self.get(request, *args, **kwargs)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_add.html"

    def get_success_url(self):
        return reverse("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_edit.html"

    def get_success_url(self):
        return reverse("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('products:home')

# from django.core.paginator import Paginator
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404, redirect, render
# from django.contrib import messages
# from catalog.models import Product
#
# from .forms import ProductForm
#
#
# def home(request):
#     product_list = Product.objects.order_by("-created_at")
#     paginator = Paginator(product_list, 5)  # 5 товаров на страницу
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     return render(request, "catalog/home.html", {"page_obj": page_obj})
#
#
# def contacts(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message_text = request.POST.get("message")
#
#         # Здесь можно добавить сохранение в базу или отправку письма
#         print(f"[Контактная форма] Имя: {name}, Телефон: {phone}, Сообщение: {message_text}")
#
#         # Добавляем сообщение об успешной отправке
#         messages.success(request, f"Спасибо, {name}! Ваше сообщение получено.")
#
#         # Можно вернуть ту же страницу, чтобы отобразилось сообщение
#         return render(request, "catalog/contacts.html")
#
#     return render(request, "catalog/contacts.html")
#
#
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, "catalog/product_detail.html", {"product": product})
#
#
# def product_add(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#     else:
#         form = ProductForm()
#     return render(request, "catalog/product_add.html", {"form": form})
#
# def product_edit(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('catalog:product_detail', pk=product.pk)
#     else:
#         form = ProductForm(instance=product)
#
#     return render(request, 'catalog/product_edit.html', {'form': form, 'product': product})
