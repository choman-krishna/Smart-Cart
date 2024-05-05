from django.contrib import admin
from cart_data.models import ItemData, ScannedItem

class ItemDataAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'bar_data', 'prize', 'item_img')

class ScannedItemAdmin(admin.ModelAdmin):
    list_display = ("user_name", "scanned_item", "in_cart")

# Register your models here.
admin.site.register(ItemData, ItemDataAdmin)
admin.site.register(ScannedItem, ScannedItemAdmin)
