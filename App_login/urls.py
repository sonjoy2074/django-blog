from django.urls import path
from App_login import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
app_name = 'App_login'  
urlpatterns = [ 
   path('signup/', views.signup, name='signup'),
   path('login/', views.login_page, name='login'),
   path('logout/', views.logout_user, name='logout'),
   path('profile/', views.profile, name='profile'),
   path('user_change/', views.user_change, name='user_change'),   
   path('password/', views.pass_change, name='pass_change'),
   path('add_profile/', views.add_pro_pic, name='add_pro_pic'),
   path('change_pro_pic/', views.change_pro_pic, name='change_pro_pic'),
]
