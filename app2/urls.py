from django.urls import path
from.import views

urlpatterns = [
    
    path('app2/',views.app2, name='app2'),
    path('ml/',views.ml, name='machine_learning'),
    path('ad/',views.ard, name='arduino'),
    path('hm/',views.home, name='home_page'),
    path('mic/',views.mic,name='microbotics'),
    path('userCform/',views.userCform, name='registration'),
    path('login/',views.login_form, name='login'),
    path('success/',views.slogin),
    path('logout/',views.logout_form, name='logout'),
    path('passC/',views.password_change, name='passwordchange'),
    path('withoutoldpass/',views.with_out_oldpass, name='withoutoldpass'),
    

    
    
    
    
]