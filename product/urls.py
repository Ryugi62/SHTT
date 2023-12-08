from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),  # 상품 목록
    path('products/add/', views.add_product, name='add_product'),  # 상품 추가
    # path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('product/delete/<int:product_id>/', views.delete_product, name='delete_product'),  # 상품 삭제
    path('delete_image/<int:image_id>/', views.delete_image, name='delete_image'),
]
