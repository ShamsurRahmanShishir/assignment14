from django.urls import path
from.import views
urlpatterns = [
    
    path('',views.app1),
    path('b/',views.bigdata),
    path('da/',views.dataanalysis),
    path('dl/',views.deep_learning),
    path('c/',views.customer_info, name='customer'),
    path('form/',views.show_form, name='cform'),
    path('successfully/',views.success, name = 'successfully'),
    path('mb/',views.microbot, name = 'microbotics'),
    path('gas/',views.gas, name = 'gas'),


    
    
]