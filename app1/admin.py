from django.contrib import admin
from .models import Info, microbotics #microbotics is my class 

# Register your models here.
class microAdmin(admin.ModelAdmin):
    list_display = ('id','customer_id','customer_name','customer_email','batch','product')

admin.site.register(microbotics,microAdmin)



class InfoAdmin(admin.ModelAdmin):
    list_display = ('First_name','Last_name','Middle_name','email','serial','password','re_password','textarea','Checkbox','payments','django')


admin.site.register(Info,InfoAdmin)
