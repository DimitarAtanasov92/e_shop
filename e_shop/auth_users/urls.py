from django.urls import path

from e_shop.auth_users.views import RegisterUserView, LogoutUserView, LoginUserView, ProfileDetailView

urlpatterns = [
    path("registration/", RegisterUserView.as_view(), name="registration"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path("login/", LoginUserView.as_view(), name="login_user"),
    path("profile-details/<int:pk>", ProfileDetailView.as_view(), name="profile_detail"),
]
