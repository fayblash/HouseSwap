from django.urls import path
from . import views

urlpatterns = [
    path('add_testimonial/',views.add_testimonial, name='add_testimonial'),
    path("update/<int:pk>/", views.update_testimonial, name="update_testimonial"),
    path("delete/<int:pk>/", views.delete_testimonial, name="delete_testimonial"),
]