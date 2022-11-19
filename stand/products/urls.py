from django.urls import path

from .views import (
    ProductList, ProductDetail, MyWorks, ProductByTag,
    about, index, contacts_and_delivery
)

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('products/', ProductList.as_view(), name='product'),
    path('product/<int:id>/', ProductDetail.as_view(), name='details'),
    path('tags/<slug:tag_slug>/', ProductByTag.as_view(), name='tag'),
    path('works/', MyWorks.as_view(), name='works'),
    path('contacts/', contacts_and_delivery, name='contacts'),
    path('about/', about, name='about')
]
