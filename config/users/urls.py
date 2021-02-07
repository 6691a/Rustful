from django.urls import path
from .views import UserCreate, BlacklistTokenUpdateView


urlpatterns = [
    path('register/', UserCreate.as_view()),
    path('logout/blacklist/',BlacklistTokenUpdateView.as_view()),
]