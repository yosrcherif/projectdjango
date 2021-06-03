from django.urls import path,include
from . import views
from django.conf.urls import url
urlpatterns=[
    path('',views.login,name='login'),
    path('register',views.register,name="register"),
    path('home',views.home,name='home'),
    path('logout',views.logout,name="logout"),
    path('addtodo',views.addtodo,name="addtodo"),
    path('delete/<id>',views.deletetodo,name="delete"),
    path('check/<id>',views.checktodo,name="check"),
    path('edit/<id>',views.edittodo,name="edit")
]

