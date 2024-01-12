from django.shortcuts import render
from django.views import generic as views

from e_shop.about_us.models import AboutUs


class AboutUsView(views.DetailView):
    model = AboutUs
    template_name = "about_us/about_us.html"
