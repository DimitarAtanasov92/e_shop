from django.urls import path

from e_shop.contacts.views import SupportCreateView

urlpatterns = [
    path("", SupportCreateView.as_view(), name="contacts")
]
