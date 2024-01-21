from django.urls import path

from e_shop.stocks.views import StocksListView, StockDetailsView

urlpatterns = [
    path("", StocksListView.as_view(), name="stocks"),
    path("<int:pk>/", StockDetailsView.as_view(), name="stocks-details"),
]
