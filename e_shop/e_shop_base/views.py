from django.views import generic as views


class BaseView(views.TemplateView):
    template_name = "base/index.html"

