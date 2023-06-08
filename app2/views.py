
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, PasswordChangeForm, SetPasswordForm
from . forms import userCf
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash



# Create your views here.
def app2(request):
    study1 = '60 days of python'
    study2 = 'learn django in 30 days'
    study3 = 'learn AI in 30 days'
    study4 = 'learn ML in 30 days'
    study_plan= {'s1':study1,'s2':study2,'s3':study3,'s4':study4}
    
    return render(request,'f2/filter.html',study_plan)
def ml(request):
    ml_learn = {'data_science':['ml','AI','007','python']}
    return render(request,'f2/ml.html',ml_learn)
def ard(request):
    return render(request,'f2/data.html')

def home(request):
    return render(request,'f2/home.html')
def mic(request):
    return render(request,'f2/mic.html')




def userCform(request):
    if request.method == 'POST':
        frm = userCf(request.POST)
        if frm.is_valid():
            frm.save()
    else:        
        frm = userCf()
    return render(request,'f2/userCform.html',{'form':frm})




def login_form(request):
    if request.method == "POST":
        frm = AuthenticationForm(request=request,data= request.POST)
        if frm.is_valid():
            uname = frm.cleaned_data['username']
            upass = frm.cleaned_data['password']
            user = authenticate(username = uname,password = upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/a2/success')
    else:        
        frm = AuthenticationForm()
    return render(request,'f2/login.html',{'form':frm})



#successfully login 
def slogin(request):
     return render(request,'f2/success.html')



#logout
def logout_form(request):
    logout(request)
    return HttpResponseRedirect('/a2/login')



#password Change
def password_change(request):
    if request.user.is_authenticated:
        if request.method == "POSt":
            frm = PasswordChangeForm(user = request.user, data = request.POST)
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request, frm.user)
                return HttpResponseRedirect('/a2/success')
        else:
            frm = PasswordChangeForm(user=request.user)
        return render(request, 'f2/passc.html',{'form':frm})
    


    else:
        return HttpResponseRedirect('/a2/login')
    

                


    

#using without old password

def with_out_oldpass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            frm = SetPasswordForm(user=request.user, data = request.POST)
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request, frm.user)
                return HttpResponseRedirect('/a2/success/')
        else:
            frm = SetPasswordForm(user=request.user)
        return render(request, 'f2/withoutpassc.html', {'form':frm})
    else:
        return HttpResponseRedirect('/a2/login/')

