from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("api_index/", views.api_index),
    path("api_create/", views.api_create),
    path("api_results/", views.api_results),
    path("api_result/<int:query_id>/", views.api_result),
    path("api_settings/", views.api_settings),
    path("api_delete_item/<int:query_id>/", views.api_delete_item),
    path("api_save_item/", views.api_save_item),
    path("api_generate_cp/", views.api_generate_cp),
]

# urlpatterns = [
#     path("", views.index, name='home'),
#     path("create/", views.create, name='create'),
#     path("delete/", views.delete, name='delete'),
#     path("edit/<int:id>/", views.edit, name='edit'),
#     path("dele/<int:id>/", views.dele, name='dele'),
#     path("contact/", TemplateView.as_view(template_name="scrap/contact.html"), name='contact'),
#     path("results/", views.results, name='results'),
#     path("result/", views.result, name='result'),
#     path("result/<int:query_id>/", views.result),
#     path("settings/", views.settings, name='settings'),
#     path("generate_cp/", views.generate_cp, name='generate_cp'),
# ]
