from django.urls.conf import path

from dwnjsn import views

urlpatterns = [
    path('jsn', views.upload_jsn, name='upload_jsn'),
    path('table', views.view_jsn, name='table_jsn'),
]