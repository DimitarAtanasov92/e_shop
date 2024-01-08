from django.urls import path

from e_shop.auth_users.views import RegisterUserView

urlpatterns = [
    path("registration/", RegisterUserView.as_view(), name="registration")
]