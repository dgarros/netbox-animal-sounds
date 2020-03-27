from django.urls import path

from . import views


# Define a list of URL patterns to be imported by NetBox. Each pattern maps a URL to
# a specific view so that it can be accessed by users.
urlpatterns = (
    path('', views.ListAnimalsView.as_view(), name='list_animals'),
    path('random/', views.RandomAnimalView.as_view(), name='random_animal'),
    path('<str:name>/', views.AnimalView.as_view(), name='animal'),
)

