from django.urls import path

from rest_framework.routers import DefaultRouter
from .views import CategoryModelViewSet
from .views import SupplierGenericListCreateApiView, SupplierGenericaRetrieveUpdateDestroyApiView
router = DefaultRouter()
router.register("category", CategoryModelViewSet)
urlpatterns = [
    path('suppliers/', SupplierGenericListCreateApiView.as_view()),
    path('suppliers/<int:id>/', SupplierGenericaRetrieveUpdateDestroyApiView.as_view())
] + router.urls