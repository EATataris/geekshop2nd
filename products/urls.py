from products.views import products, basket_add, basket_remove, basket_edit
from django.urls import path

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('add/<int:product_id>/', basket_add, name='basket_add'),
    path('remove/<int:id>/', basket_remove, name='basket_remove'),
    path('edit/<int:id>/<int:quantity>/', basket_edit, name='basket_edit'),
]