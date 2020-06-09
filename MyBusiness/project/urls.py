from django.urls import path
from . import views
urlpatterns=[
    path('register',views.registerPage,name='register'),
    path('login',views.loginPage,name='login'),
    path('logout',views.logoutPage,name='logout'),
    path('',views.my_html, name='my_html'),
    path('add1',views.add1, name='add1'),
    path('update/<str:pk>/',views.update, name='update'),
    path('delete_product/<str:pk>/',views.delete_product, name='delete_product'),
    path('show/<str:pk>/',views.show, name='show'),
    path('sell_product/<str:pk>/',views.sell_product, name='sell_product'),
    path('sell',views.sell, name='sell'),
    path('sell_delete/<str:pk>/',views.sell_delete, name='sell_delete'),
]
