from django.conf.urls import url
from django.urls import path, include

from .views import (
    UserApiView,
    UserDetailsView
)


urlpatterns = [
    path('user', UserApiView.as_view()),
    path('user/<int:user_id>', UserDetailsView.as_view()),
]
