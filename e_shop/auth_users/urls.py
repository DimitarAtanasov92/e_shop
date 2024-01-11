from django.urls import path

from e_shop.auth_users.views import RegisterUserView, LogoutUserView, LoginUserView, ProfileDetailView, \
    ProfileDeleteView, ProfileUpdateView

urlpatterns = [
    path("registration/", RegisterUserView.as_view(), name="registration"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path("login/", LoginUserView.as_view(), name="login_user"),
    path("profile-details/<int:pk>", ProfileDetailView.as_view(), name="profile_detail"),
    path("profile-delete/<int:pk>", ProfileDeleteView.as_view(), name="profile_delete"),
    path("profile-edit/<int:pk>", ProfileUpdateView.as_view(), name="profile_edit"),
]
