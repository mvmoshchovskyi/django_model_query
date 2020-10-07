from django.urls import path
from .views import OfficeViews

urlpatterns = [
    path('', OfficeViews.as_view())
]
