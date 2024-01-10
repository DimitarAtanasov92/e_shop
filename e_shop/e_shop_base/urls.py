from django.urls import path

from e_shop.e_shop_base.views import BaseView

urlpatterns = [
    path("", BaseView.as_view(), name="index"),
]
