from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','choose','name', 'email', 'address','products', 'quantity', 'packaging', 'date')
   