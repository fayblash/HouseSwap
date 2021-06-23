from django.urls import path
from .import views  

urlpatterns = [ 
    path('offer_trade/<int:pk>/', views.offer_trade,name='offer_trade'),
    # path("update/<int:pk>/", views.update_offer, name="update_offer"),
    path("delete/<int:pk>/", views.delete_offer, name="delete_offer"),
    # path("accept/<int:pk>/", views.accept_offer, name="accept_offer"),
    # path("reject/<int:pk>/", views.reject_offer, name="reject_offer"),
]
