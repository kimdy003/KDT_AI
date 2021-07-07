from django.contrib import admin
from .models import Coffee

# Register your models here.
# 어떤 모델이 있을 때 이 모델을 자연스럽게 관리할 수 있다.
admin.site.register(Coffee)
