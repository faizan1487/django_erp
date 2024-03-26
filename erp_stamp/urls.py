from django.urls import path
from .views import item_list_view

urlpatterns = [
    path('', item_list_view, name='item_list'),
    # Add other URL patterns as needed
]
