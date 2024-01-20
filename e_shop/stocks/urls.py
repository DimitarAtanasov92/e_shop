from django.urls import path

from e_shop.stocks.views import StocksListView


urlpatterns = [
    path("", StocksListView.as_view(), name="stocks")
]
