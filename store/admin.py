from django.contrib import admin

# Register your models here.

from .models import *

class ImagesTabularInline(admin.TabularInline):
    model = Images

class TagTabularInline(admin.TabularInline):
    model = Tag

class ProductAdmin(admin.ModelAdmin):
    inlines =  [ImagesTabularInline,TagTabularInline]
  
class OrderItemTabularinline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTabularinline]
    list_display = ['firstname','phone','email','payment_id','paid','date']
    search_fields=['firstname','email','payment_id']


admin.site.register(Images)
admin.site.register(Tag)

admin.site.register(Categories)
admin.site.register(Collections)

admin.site.register(Filter_Price)
admin.site.register(Product,ProductAdmin)
admin.site.register(Contact_us)

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Cart)




