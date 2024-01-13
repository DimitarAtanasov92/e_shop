from django.shortcuts import render, redirect
from django.views import generic as view

from e_shop.e_shop_base.models import Profile
from e_shop.events.forms import CommentEventForm
from e_shop.events.models import Event


class EventsListView(view.ListView):
    model = Event
    template_name = "events/events_list.html"
    paginate_by = 3


class EventsDetailsView(view.DetailView):
    model = Event
    template_name = "events/event_detail.html"


def add_comment(request, pk):
    if request.method == 'POST':
        form = CommentEventForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_event = Event.objects.get(id=pk)
            comment.to_profile = Profile.objects.get(user=request.user)
            comment.save()
            return redirect('events_list')
    else:
        form = CommentEventForm()
    return render(request, 'events/add_comment.html', {'form': form})
