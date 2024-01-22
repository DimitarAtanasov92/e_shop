from django.shortcuts import render
from django.views import generic as view
from django.contrib.auth import mixins as auth_mixins
from e_shop.stocks.models import Stock, Purchase
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy


class StocksListView(view.ListView):
    model = Stock
    template_name = "stocks/stocks.html"


class StockDetailsView(view.DetailView):
    model = Stock
    template_name = "stocks/stock_details.html"


class PurchaseCreateView(auth_mixins.LoginRequiredMixin, view.CreateView):
    model = Purchase
    fields = ["address", "phone"]
    template_name = "stocks/purchase.html"
    success_url = reverse_lazy('stocks')

    def form_valid(self, form):
        product = get_object_or_404(Stock, pk=self.kwargs['pk'])
        form.instance.product = product
        form.instance.email = self.request.user.email
        return super().form_valid(form)

