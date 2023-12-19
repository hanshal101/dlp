from django.urls import path
from django import views
from .views import import_csv,studentData

urlpatterns = [
    path('import-csv/', import_csv, name='import_csv'),
    path('studentData/',studentData,name='studentData')
]
