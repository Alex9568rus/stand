from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, Tag, Works


def index(request):
    """Функция для отображения начальной(главной) страницы."""
    title = 'siberia Cake | Торты на заказ'
    template = 'products/index.html'
    context = {'title': title}
    return render(request, template, context)


class ProductList(ListView):
    """Класс представления всего ассортимента."""
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'obj_on_display'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продукция'
        context['tags'] = Tag.objects.all()
        return context


class ProductDetail(DetailView):
    """Класс предствления определённого продукта."""
    model = Product
    template_name = 'products/details.html'
    pk_url_kwarg = 'id'
    context_object_name = 'cake'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['cake']
        return context


class ProductByTag(ProductList):

    def get_queryset(self):
        return Product.objects.filter(tag__slug=self.kwargs['tag_slug'])


class MyWorks(ProductList):
    """Класс представления конечных продуктов (готовых тортов, рулетов и т.д).
    """
    model = Works
    template_name = 'products/my_works.html'
    extra_context = {'title': 'Мои работы'}


class WorksByTags(ProductByTag):

    def get_queryset(self):
        return Works.objects.filter(tag__slug=self.kwargs['tag_slug'])


def contacts_and_delivery(request):
    """Функция для отображения контактов и условий доставки."""
    title = 'Контакты и доставка'
    template = 'products/contacts.html'
    context = {'title': title}
    return render(request, template, context)


def about(request):
    """Функция для отображения информации о себе."""
    title = 'Обо мне'
    template = 'products/about.html'
    context = {'title': title}
    return render(request, template, context)
