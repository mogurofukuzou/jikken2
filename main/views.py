from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group, Permission
from .models import Manager

from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponseServerError
# Create your views here.






def index(request):
    return render(request,"home.html")

def jikken(request):
    return render(request,"jikken.html")


def mylogin(request):

    if request.method == 'POST':

        utxt = request.POST.get('username')   # utxt to get/receive the username
        ptxt = request.POST.get('password')   # ptxt to get/receive the password   

        if utxt != "" and ptxt != "":

            user = authenticate(username=utxt, password=ptxt) 

            if user != None:

                login(request, user)
                return redirect('panel')

    return render(request, 'login2.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        
        user = User.objects.create_user(name,email,password1)
        #user.save()
        #b = Manager(name=name, username=uname, email=email)
        #b.save()
        print("save")

        return render(request,'login2.html')

        
    return render(request, 'register.html')
def myregister(request):

    if request.method == 'POST':
        
        name = request.POST.get('name')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if name == "" :
            msg = "Input Your Name"
            return render(request, 'front/msgbox.html', {'msg':msg})

        if password1 != password2 :
            msg = "Your Password Didn't Match"
            return render(request, 'front/msgbox.html', {'msg':msg})

    #-# Check Password is Weak or Strong (by using count) Start #-#
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        for i in password1 :
            ## I defined here 4 counts
            ## if any user enter 10 char, count will change from 1 to 1 and it won't increase
            ## If my count 1 2 3 and 4 were all 1 then my password is a strong password
            if i > "0" and i < "9" :
                count1 = 1              ## one number, count will change from 0 to 1
            if i > "A" and i < "Z" :
                count2 = 1              ## one cap letter, count will change from 0 to 1
            if i > "a" and i < "z" :
                count3 = 1              ## one small letter, count will change from 0 to 1
            if i > "!" and i < "(" :
                count4 = 1              ## one sign, count will change from 0 to 1
            ## if enter number,cap,small,sign(count 1 1 1 1). if enter number,small(count 1 0 1 0) ## 
        if count1 == 0 or count2 == 0 or count3 == 0 and count4 == 0 :
            msg = "Your Password Is Not Strong Enough"
            return render(request, 'front/msgbox.html', {'msg':msg})
    #-# Check Password is Weak or Strong (by using count) End #-#
        if len(password1) < 8 :
            msg = "Your Password Must Be At Least 8 Characters"
            return render(request, 'front/msgbox.html', {'msg':msg})

        if len(User.objects.filter(username=uname)) == 0 and len(User.objects.filter(email=email)) == 0 :

            # Get User IP Start
            """
            ip, is_routable = get_client_ip(request)

            if ip is None:
                ip = "0.0.0.0"
            # Get User IP End
            # Get User Location Start
            try:
                response = DbIpCity.get(ip, api_key='free')
                country = response.country + " | " + response.city

            except:
                country = "Unknown"
            # Get User Location End
            """
            
            user = User.objects.create_user(username=uname, email=email, password=password1)
            user.save()
            #b = Manager(name=name, username=uname, email=email)
            #b.save()

    return render(request, 'login2.html')



def panel(request):
    if not request.user.is_authenticated:
        return(redirect('mylogin'))
    return render(request,'back/home.html')




def signup(request):
    return render(request,"signup.html")


def form_login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'form_login.html', {'form': form})



@requires_csrf_token
def my_customized_server_error(request, template_name='500.html'):
    import sys
    from django.views import debug
    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponseServerError(error_html)













