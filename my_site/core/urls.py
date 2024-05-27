
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from my_site.settings import MEDIA_URL, MEDIA_ROOT

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'programmerView', ProgrammerViewSet)

urlpatterns = [

    path('api/v1/', include(router.urls))  #api/v1/programmerView/

    # path('programmer/', Programmer.as_view())

    # path('api/v1/programmerView/', ProgrammerViewSet.as_view({'get': 'list'})),
    # path('api/v1/programmerView/<int:pk>/', ProgrammerViewSet.as_view({'put': 'update'}))
]

if settings.DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)