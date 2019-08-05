from django.conf.urls import url
from basic_CRUD_app import views

app_name = 'basic_CRUD_app'

urlpatterns = [
    # -------------------------------------------Templates-------------------------------------------------------------
    url(r'^$', views.login_page, name='signin'),

    url(r'^superadmin/tasks/(?P<id>[\w\-]+)$', views.admin_tasks_page, name='admin_tasks_page'),
    url(r'^addTask/(?P<id>[\w\-]+)$', views.admin_add_tasks_page, name='admin_add_tasks_page'),
    url(r'^addTaskLogic/(?P<id>[\w\-]+)$', views.addTaskLogic, name='addTaskLogic'),




    url(r'^user/tasks/(?P<id>[\w\-]+)$', views.user_tasks_page, name='user_tasks_page'),

    # -------------------------------------------API-------------------------------------------------------------
    url(r'^login/$', views.LoginAPI.as_view(), name='LoginAPI'),
    url(r'^tasks/', views.TasksAPI.as_view(), name='TasksAPI'),
    url(r'^taskAction/(?P<id>[\w\-]+)$', views.TaskActionAPI.as_view(), name='TaskActionAPI'),

]