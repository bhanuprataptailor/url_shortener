from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ShortUrlView, CreateUrlView

urlpatterns = [
    path('<pk>/', ShortUrlView.as_view()),
    path('generate_url', CreateUrlView.as_view()),
]
