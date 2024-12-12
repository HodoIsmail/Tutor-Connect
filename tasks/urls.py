from django.urls import path
from . import views

urlpatterns = [
      # path('', views.index , name="home"),
      path('', views.task_details, name='tasks'),
      path('update_task/<str:pk>/', views.update_task, name='update task'),
      path('delete_task/<str:pk>/', views.delete_task, name='delete task')
]
