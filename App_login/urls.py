from django.urls import path
from App_login import views
app_name = 'App_login'  
urlpatterns = [ 
   path('signup/', views.signup, name='signup'),
   path('login/', views.login_page, name='login'),
   path('logout/', views.logout_user, name='logout'),
]