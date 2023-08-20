from django.urls import path

from app.propiedad.views import propiedad_list_view, propiedad_create_view, propiedad_update_view, \
    propiedad_delete_view, propiedad_detail_view

app_name = "propiedad"

urlpatterns = [
    path('', propiedad_list_view, name='propiedad-list'),
    path('create/', propiedad_create_view, name='propiedad-create'),
    path('<int:pk>/', propiedad_detail_view, name='propiedad-detail'),
    path('update/<int:pk>/', propiedad_update_view, name='propiedad-update'),
    path('delete/<int:pk>/', propiedad_delete_view, name='propiedad-delete'),
]
