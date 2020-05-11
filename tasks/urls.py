from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('',views.index,name='index'),
    path('update/<int:pk>/',views.update,name='update'),
    path('delete/<int:pk>/',views.deletetask,name='delete'),
]
