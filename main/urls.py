from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('', views.index, name="index"),
    path('task/add/<int:task_id>', views.task_add, name='task_add'),
    path('task/del/<int:task_id>', views.task_delete, name='task_delete'),
    path('task/fin/<int:task_id>', views.task_finish, name='task_finish'),
    path('task/plus/<int:task_id>', views.task_stat_plus, name="task_plus"),
    path('task/minus/<int:task_id>', views.task_stat_minus, name="task_minus"),
]
