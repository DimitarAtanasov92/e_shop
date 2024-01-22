from django.urls import path

from e_shop.stocks.views import StocksListView, StockDetailsView, PurchaseCreateView

urlpatterns = [
    path("", StocksListView.as_view(), name="stocks"),
    path("<int:pk>/", StockDetailsView.as_view(), name="stocks-details"),
    path("purchase/<int:pk>/", PurchaseCreateView.as_view(), name="purchase"),
]
