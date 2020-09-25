from django.conf.urls import url, include
from django.urls import path
from sa_api import views
from sa_api import templates

urlpatterns = [
    path('dashboard', views.dashboard),
    path('summary_rosette', views.summary_rosette),
    path('summary_file', views.summary_file),
    path('upload_review', views.upload_review),
    path('review', views.review),
    path('get_wavedata', views.get_wavedata),
    path('get_numberdata', views.get_numberdata),
    path('comment_annotation', views.comment_annotation),
    path('delete_annotation', views.delete_annotation),
    path('add_annotation', views.add_annotation),
    path('like_annotation', views.like_annotation),
    path('catch',views.func_test, name='test'),
    path('test_query',views.test_query),
    path('get_annotation', views.get_annotation),
    path('dashboard_rosette',views.func_test),
    path('download_vital_file', views.download_vital_file),
    path('download_csv_device', views.download_csv_device),
    path('server/device_info', views.device_info_server),
    path('server/channel_info', views.channel_info_server),
    path('server/client_info', views.client_info_server),
    path('server/device_list', views.device_list_server),
    path('server/channel_list', views.channel_list_server),
    path('server/recording_info', views.recording_info_server),
    path('client/device_info', views.device_info_client),
    path('client/channel_info', views.channel_info_client),
    path('client/client_info', views.client_info_client),
    path('client/recording_info', views.recording_info_client),
    path('client/report_status', views.report_status_client),
    path('client/device_list', views.device_list_client),
    path('client/channel_list', views.channel_list_client),
    path('migration/register_vital_file', views.register_vital_file),
    path('login', views.login),

    #study jango
    path('css_test', views.css_test),
    path('test_jango/<str:name>', views.test_jango),
    path('throw',views.throw),
    path('catch',views.catch),
    path('Comment',views.Comment),
    path('MBP_graph',views.mpb_graph),
    path('dashboard_device',views.Dashboard_device),

]
