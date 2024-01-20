from django.contrib import admin

from e_shop.stocks.models import ImgStocks, Stock


class ImgStockInLineAdmin(admin.TabularInline):
    model = ImgStocks


@admin.register(ImgStocks)
class ImgStocksAdmin(admin.ModelAdmin):
    list_display = ["stocks"]


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [
        ImgStockInLineAdmin,
    ]
