from django.shortcuts import render
from app1.models import microbotics
from . forms import customerRegistration
from django.http import HttpResponseRedirect
from . models import Info

# Create your views here.
def app1(request):
    return render(request,'f1/login.html')
def bigdata(request):
    return render(request,'f1/bdata.html')
def dataanalysis(request):
    return render(request,'f1/dataanalysis.html')
def deep_learning(request):
    return render(request,'f1/dl.html')

def microbot(request):
    return render(request,'f1/new.html')

def gas(request):
    return render(request,'f1/gas.html')





def customer_info(request):
    cdetails = microbotics.objects.all()
    return render(request, 'f1/cust.html',{'cust':cdetails})



def show_form(request):
    if request.method == "POST":
        frm = customerRegistration(request.POST)
        if frm.is_valid():
            
            
            
            fname =  frm.cleaned_data['Enter_First_name']
            mname =  frm.cleaned_data['Enter_Middle_name']
            lname =  frm.cleaned_data['Enter_Last_name']
            eml = frm.cleaned_data['email']
            ser =  frm.cleaned_data['serial']
            pas = frm.cleaned_data['password']
            rpas =  frm.cleaned_data['re_password']
            txt =  frm.cleaned_data['textarea']
            chk = frm.cleaned_data['checkbox']
            pay =  frm.cleaned_data['payments']
            dj = frm.cleaned_data['django']



            djangotwo = Info(First_name=fname,Middle_name=mname,Last_name=lname,email=eml,serial=ser,password=pas,re_password=rpas,textarea=txt,Checkbox=chk,payments=pay,django=dj)
            djangotwo.save()


            return HttpResponseRedirect('/successfully/')
            


       

    else:   
        frm = customerRegistration(auto_id='customer_%s', label_suffix='=' ,initial={'email':'theonsesrs@gmail.com'} )
        print("Execute GET")
    #frm.order_fields(field_order=['email','Last_name','serial','First_name'])
    return render(request,'f1/forms.html',{'form':frm})




def success(request):
    return render(request,'f1/submit.html')






 

    

 