from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.api_applications.views import APIApplicationViewSet, APIApplicationResetKeyView, APIApplicationTestDetailView

api_applications_router = DefaultRouter()
api_applications_router.register('', APIApplicationViewSet)

urlpatterns = [
    path('<uuid:pk>/reset_key/', APIApplicationResetKeyView.as_view()),
    path('test/', APIApplicationTestDetailView.as_view())
]

urlpatterns += api_applications_router.urls