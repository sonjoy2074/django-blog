from django.urls import path
from App_login import views
app_name = 'App_login'  
urlpatterns = [ 
   path('signup/', views.signup, name='signup'),
]