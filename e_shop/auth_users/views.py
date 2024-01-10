from django.contrib.auth import login
from e_shop.auth_users.form import RegisterUserForm
from django.contrib.auth import views as auth_views
from django.views import generic as views
from django.urls import reverse_lazy
from e_shop.e_shop_base.models import UserModel, Profile


class RegisterUserView(views.CreateView):
    template_name = "auth_users/register.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginUserView(auth_views.LoginView):
    template_name = "auth_users/login.html"


class LogoutUserView(auth_views.LogoutView):
    pass


class ProfileDetailView(views.DetailView):
    model = Profile
    template_name = 'auth_users/profile_detail.html'


class ProfileDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'auth_users/delete_profile.html'
    success_url = reverse_lazy('index')


class ProfileUpdateView(views.UpdateView):
    model = Profile
    fields = ["img", "first_name", "last_name", "age"]
    template_name = 'auth_users/edit_profile.html'
    success_url = reverse_lazy('index')
