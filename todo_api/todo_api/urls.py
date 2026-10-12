
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet
from django.http import HttpResponse
from pathlib import Path

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

def home(request):
    file_path = Path(__file__).resolve().parent.parent.parent / 'index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        return HttpResponse(f.read())

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]