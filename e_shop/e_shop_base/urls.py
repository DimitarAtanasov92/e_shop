from django.urls import path

from e_shop.e_shop_base.views import BaseView, LogoutUserView

urlpatterns = [
    path("", BaseView.as_view(), name="index"),
    path("logout/", LogoutUserView.as_view(), name="logout")
]
