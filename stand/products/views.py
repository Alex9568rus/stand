from django.views.generic import ListView, DetailView, TemplateView

from .models import Product, Works
from .utils import ContextDataMixin


class Index(TemplateView):
    """Класс для отображения начальной(главной) страницы."""
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Siberia Cake | Торты на заказ'
        return context


class ProductList(ContextDataMixin, ListView):
    """Класс представления всего ассортимента."""
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'obj_on_display'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_data = self.get_user_context(title='Siberia Cake | Ассортимент')
        return dict(list(context.items()) + list(add_data.items()))

    def get_queryset(self):
        return Product.objects.select_related('tag')


class ProductDetail(DetailView):
    """Класс предствления определённого продукта."""
    model = Product
    template_name = 'products/details.html'
    pk_url_kwarg = 'id'
    context_object_name = 'cake'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Siberia Cake | ' + str(context['cake'])
        return context


class ProductByTag(ProductList):
    """Распределение продукцие по тегам."""

    def get_queryset(self):
        return Product.objects.filter(tag__slug=self.kwargs['tag_slug'])


class MyWorks(ContextDataMixin, ListView):
    """Класс представления конечных продуктов (готовых тортов, рулетов и т.д).
    """
    model = Works
    template_name = 'products/my_works.html'
    context_object_name = 'obj_on_display'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_data = self.get_user_context(title='Siberia Cake | Мои работы')
        return dict(list(context.items()) + list(add_data.items()))

    def get_queryset(self):
        return Works.objects.select_related('tag')


class WorksByTags(MyWorks):
    """Распределение моих работ по тегам."""

    def get_queryset(self):
        return Works.objects.filter(tag__slug=self.kwargs['tag_slug'])


class ContactsAndDelivery(TemplateView):
    """Класс для отображения контактов и условий доставки."""
    title = 'Siberia Cake | Контакты и доставка'
    template_name = 'products/contacts.html'
    extra_context = {'title': title}


class About(TemplateView):
    """Класс для отображения информации о себе."""
    title = 'Siberia Cake | Обо мне'
    template_name = 'products/about.html'
    extra_context = {'title': title}
