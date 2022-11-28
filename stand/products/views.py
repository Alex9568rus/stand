from django.views.generic import ListView, DetailView, TemplateView

from .models import Product, Tag, Works


class Index(TemplateView):
    """Класс для отображения начальной(главной) страницы."""
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Siberia Cake | Торты на заказ'
        return context


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
        context['tag_names'] = ['Бисквитные торты', 'Бенто-торты']
        return context


class ProductByTag(ProductList):
    """Распределение продукцие по тегам."""
    def get_queryset(self):
        return Product.objects.filter(tag__slug=self.kwargs['tag_slug'])


class MyWorks(ListView):
    """Класс представления конечных продуктов (готовых тортов, рулетов и т.д).
    """
    model = Works
    template_name = 'products/my_works.html'
    extra_context = {'title': 'Мои работы'}
    context_object_name = 'obj_on_display'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои работы'
        context['tags'] = Tag.objects.all()
        return context


class WorksByTags(MyWorks):
    """Распределение моих работ по тегам."""

    def get_queryset(self):
        return Works.objects.filter(tag__slug=self.kwargs['tag_slug'])


class ContactsAndDelivery(TemplateView):
    """Класс для отображения контактов и условий доставки."""
    title = 'Контакты и доставка'
    template_name = 'products/contacts.html'
    extra_context = {'title': title}


class About(TemplateView):
    """Класс для отображения информации о себе."""
    title = 'Обо мне'
    template_name = 'products/about.html'
    extra_context = {'title': title}
