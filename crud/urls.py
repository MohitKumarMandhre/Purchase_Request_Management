from django.urls import path , re_path
from . import views
from django.conf.urls import url

app_name = 'crud' 

urlpatterns = [
    path('', views.Post_list, name='postList'),
    path('fill/', views.Post_data, name='postdata'),
    path('fill2/', views.postData2, name='postData2'),
    path('remove2/<int:id>/', views.delete_view2 , name = "delete_view2" ),
    path('update2/<int:id>/', views.update_view2 , name = "update_view2" ),
    path('remove/<int:id>/', views.delete_view , name = "delete_view" ),
    path('update/<int:id>/', views.update_view , name ="update_view") ,
    path('list/', views.list_view , name="list_view"),
    path('open/<int:id>/', views.open , name ="open" ),
    # path('fill/delete_item/<int:pk>', views.delete_item, name="delete_item"),
    # path('dUpdate/<int:product_id>/', views.dUpdate, name='dUpdate' ),
    # url(r'^edit/update(?P<id>\d+)$', views.update, name="update" )
    # path('fill/<int:pk>/', views.dUpdate, name='dUpdate')
    # re_path(r'^auto/$', views.auto, name='autoC'),
]
