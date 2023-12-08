from django.db import models
from datetime import datetime
import os
import uuid

def generate_unique_filename(instance, filename):
    ext = filename.split('.')[-1]
    unique_filename = f"{uuid.uuid4()}.{ext}"
    today = datetime.today()
    year = today.year
    month = today.strftime('%m')
    day = today.strftime('%d')
    return os.path.join('product_images', str(year), month, day, unique_filename)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

def product_image_path(instance, filename):
    # 원본 이미지 파일 이름 그대로 사용하고, 'product_images/연도/월/일/' 경로에 저장
    return os.path.join('product_images', instance.image.name)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=generate_unique_filename)

    def __str__(self):
        return f"Image for {self.product.name}"
