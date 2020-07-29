from django.urls import path
from django.views.generic import TemplateView

from . import views
urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    path("function/", views.index, name="function"),
    # path("class/", views.all_view, name="class")
]