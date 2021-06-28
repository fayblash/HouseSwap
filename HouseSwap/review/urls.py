from django.urls import path
from . import views

urlpatterns = [
    path('add_review/<int:pk>/',views.add_review, name='add_review'),
    path("update/<int:pk>/", views.update_review, name="update_review"),
    path("delete/<int:pk>/", views.delete_review, name="delete_review"),
]