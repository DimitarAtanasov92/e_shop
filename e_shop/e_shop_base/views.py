from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views import generic as views
from django.urls import reverse_lazy
from e_shop.e_shop_base.models import UserModel, Profile


class BaseView(views.TemplateView):
    template_name = "base/index.html"


class LoginUserView(auth_views.LoginView):
    template_name = "base/login.html"


class LogoutUserView(auth_views.LogoutView):
    pass


class ProfileDetailView(views.DetailView):
    model = Profile
    template_name = 'base/profile_detail.html'


class ProfileDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'base/delete_profile.html'
    success_url = reverse_lazy('index')


class ProfileUpdateView(views.UpdateView):
    model = Profile
    fields = ["img", "first_name", "last_name", "age"]
    template_name = 'base/edit_profile.html'
    success_url = reverse_lazy('index')
