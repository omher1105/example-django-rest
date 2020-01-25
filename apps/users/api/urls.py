
from django.urls import path

from apps.users.api.views import UserViewSets

urlpatterns = [
    path('', UserViewSets.as_view()),
    path('<int:pk>', UserViewSets.as_view())
]
