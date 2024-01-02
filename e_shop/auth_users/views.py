from django.contrib.auth import login
from django.shortcuts import render
from django.views import generic as views
from django.urls import reverse_lazy
from e_shop.auth_users.form import RegisterUserForm


class RegisterUserView(views.CreateView):
    template_name = "auth_users/register.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result
