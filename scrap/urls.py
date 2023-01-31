from django.urls import path
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
