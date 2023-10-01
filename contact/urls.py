from django.urls import include, path
from rest_framework import routers
from .viewsets import ContactFormViewSet

router = routers.DefaultRouter()
router.register(r'', ContactFormViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
    # path('network-data/', GetNetworkDataView.as_view(), name='network-data'),
    # path('node_search/', NodeSearch.as_view(), name='node_search'),  # Add this line
]
