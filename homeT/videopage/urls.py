from django.urls import path
from . import views

app_name='videopage'
urlpatterns = [ 
    path('', views.partHome, name="partHome"),
    path("partHomeDetail/<int:id>", views.partHomeDetail, name="partHomeDetail"),
    path('createPart/', views.createPart, name="createPart"),
    path("hashtags/<int:id>/", views.hashtaging, name="hashtags"),
    path("reviewsDelete/<int:id>", views.reviewsDelete, name="reviewsDelete"),
]
    