from django.shortcuts import render
from django.views import generic as view

from e_shop.stocks.models import Stock


class StocksListView(view.ListView):
    model = Stock
    template_name = "stocks/stocks.html"


class StockDetailsView(view.DetailView):
    model = Stock
    template_name = "stocks/stock_details.html"

