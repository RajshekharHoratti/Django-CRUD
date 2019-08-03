from django.conf.urls import url
from basic_CRUD_app import views

app_name = 'basic_CRUD_app'

urlpatterns = [
    url(r'^$', views.login_page, name='signin'),
    url(r'^superadmin/dashboard/(?P<id>[\w\-]+)$', views.admin_dashboard_page, name='admin_dashboard_page'),

    url(r'^superadmin/tasks/(?P<id>[\w\-]+)$', views.admin_tasks_page, name='admin_tasks_page'),






    url(r'^login/$', views.LoginAPI.as_view(), name='LoginAPI'),

]