from django.urls import path

from .views import (
    ProductList, ProductDetail, MyWorks, ProductByTag, WorksByTags,
    About, Index, ContactsAndDelivery
)

app_name = 'products'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('products/', ProductList.as_view(), name='product'),
    path('product/<int:id>/', ProductDetail.as_view(), name='details'),
    path('tags/<slug:tag_slug>/', ProductByTag.as_view(), name='prod_by_tag'),
    path('works/', MyWorks.as_view(), name='works'),
    path('works/<slug:tag_slug>/', WorksByTags.as_view(), name='work_by_tag'),
    path('contacts/', ContactsAndDelivery.as_view(), name='contacts'),
    path('about/', About.as_view(), name='about')
]
