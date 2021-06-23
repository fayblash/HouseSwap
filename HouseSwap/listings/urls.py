from django.urls import path
from .import views  

urlpatterns = [ 
    path('add_listing/', views.add_listing,name='add_listing'),
    path("update/<int:pk>/", views.update_listing, name="update_listing"),
    path("delete/<int:pk>/", views.delete_listing, name="delete_listing"),
    path("listing/<int:pk>",views.listing,name='listing'),
    path("listings",views.listings,name='listings'),
]
