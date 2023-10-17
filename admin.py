from django.contrib import admin
from .models import Todo, Student
from .models import Category
from .models import Product

admin.site.register(Todo)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Student)