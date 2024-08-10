from django.urls import path
from sistemaB import views
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('navBar/', views.navBar, name='navBar'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('personal/', views.personal, name='personal'),
    path('reportes/', views.reportes, name='reportes'),
   
    
]