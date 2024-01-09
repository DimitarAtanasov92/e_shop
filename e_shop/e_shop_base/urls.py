from django.urls import path

from e_shop.e_shop_base.views import BaseView, LogoutUserView, LoginUserView

urlpatterns = [
    path("", BaseView.as_view(), name="index"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path("login/", LoginUserView.as_view(), name="login_user"),
]
