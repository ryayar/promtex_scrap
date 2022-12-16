from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("create/", views.create, name='create'),
    path("edit/<int:id>/", views.edit, name='edit'),
    path("delete/", views.delete, name='delete'),
    path("dele/<int:id>/", views.dele, name='dele'),
    path("contact/", TemplateView.as_view(template_name="scrap/contact.html"), name='contact'),
    path("results/", views.results, name='results'),
    path("result/", views.result, name='result'),
    path("result/<int:query_id>/", views.result),
    path("generate_cp/", views.generate_cp, name='generate_cp'),
]