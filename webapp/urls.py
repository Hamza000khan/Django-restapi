from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', csrf_exempt(views.ItemsList.as_view())),
    path('delete/<int:id>', csrf_exempt(views.ItemsList.as_view())),
    path('update/<int:id>', csrf_exempt(views.ItemsList.as_view())),
    path('edit/<int:id>', views.edit, name='edit'),
]