from django.urls import path

from e_shop.events import views
from e_shop.events.views import EventsListView, EventsDetailsView

urlpatterns = [
    path("list/", EventsListView.as_view(), name="events_list"),
    path("list/<int:pk>", EventsDetailsView.as_view(), name="event_details"),
    path("list/<int:pk>/add/", views.add_comment, name="add_comment"),
]
