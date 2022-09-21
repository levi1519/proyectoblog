from xml.dom.minidom import Document
from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns=[
    path('', views.inicio, name='inicio'),
    path('ropas', views.ropas, name='ropas'),
    path('ropas/crear', views.crear, name='crear'),
    path('ropas/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('ropas/editar/<int:id>', views.editar, name='editar'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)