
from django.urls import path,include
from u import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.log_view,name='login'),
    path('index/',views.index_view,name='index'),
    path('wregister/',views.wregister,name='wregister'),
    # path('index/search/<int:pk>/',views.search,name='search'),


]
   
