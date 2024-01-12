from django.urls import path

from e_shop.about_us.views import AboutUsView

urlpatterns = [
    path("<int:pk>/", AboutUsView.as_view(), name="about_us"),
]