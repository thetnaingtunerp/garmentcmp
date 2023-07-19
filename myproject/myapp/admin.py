from django.contrib import admin
from .models import *
# Register your models here.
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'BuyerName','Address')
admin.site.register(Buyer,BuyerAdmin)

class StyleAdmin(admin.ModelAdmin):
    list_display = ('id', 'BuyerName','StyleCode','ItemName')
admin.site.register(Style,StyleAdmin)

class ProductionLineAdmin(admin.ModelAdmin):
    list_display = ('id', 'ProductionLine')
admin.site.register(ProductionLine,ProductionLineAdmin)

class ProductionInputAdmin(admin.ModelAdmin):
    list_display = ('id', 'line', 'style','input_qty','date')
admin.site.register(ProductionInput,ProductionInputAdmin)


class DailyProductionOuputAdmin(admin.ModelAdmin):
    list_display = ('id', 'line', 'style')
admin.site.register(DailyProductionOuput,DailyProductionOuputAdmin)

class DailyProductionLineMenPowerAdmin(admin.ModelAdmin):
    list_display = ('line','num_operator','num_helper','date')
admin.site.register(DailyProductionLineMenPower,DailyProductionLineMenPowerAdmin)

class AccVariantAdmin(admin.ModelAdmin):
    list_display = ('accinv','size','quantity','remark')
admin.site.register(AccVariant,AccVariantAdmin)

admin.site.register(OrderQty)

admin.site.register(AccInventoy)


admin.site.register(AccImage)
admin.site.register(WareHouse)
admin.site.register(AccessoriesRequestToWh)