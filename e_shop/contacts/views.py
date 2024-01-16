from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from e_shop.contacts.models import ContactUs


class SupportCreateView(views.CreateView):
    model = ContactUs
    template_name = 'contacts/contacts.html'
    fields = ["title", "message", "email"]
    success_url = reverse_lazy('contacts')
