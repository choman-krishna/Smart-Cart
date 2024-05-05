from django.contrib import admin
from cart_data.models import ItemData

class ItemDataAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'bar_data', 'prize', 'item_img')


# Register your models here.
admin.site.register(ItemData, ItemDataAdmin)
