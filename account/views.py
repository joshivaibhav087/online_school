from django.shortcuts import render,redirect
from .forms import LoginForm, ProfileForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Register
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth import authenticate,login,logout
from teacher.models import Admin
from django.views.generic import ListView

# Create your views here.

class Home(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'home.html')
    
# @method_decorator(login_required, name = 'dispatch')
class registerview(View):
    def post(self, *agrs, **kwargs):
        f1 = RegisterForm(self.request.POST)
        f2 = ProfileForm(self.request.POST, self.request.FILES)
        if f1.is_valid() and f2.is_valid():
            username = f1.cleaned_data['username']
            first_name = f1.cleaned_data['first_name']
            last_name = f1.cleaned_data['last_name']
            email = f1.cleaned_data['email']
            password = f1.cleaned_data['password']
            password1 = f1.cleaned_data['password1']

            phone_no = f2.cleaned_data['phone_no']
            age = f2.cleaned_data['age']
            id_proof = f2.cleaned_data['id_proof']
            gender = f2.cleaned_data['gender']
            class1 = f2.cleaned_data['class1']
            user = User.objects.create_user(username=username, first_name=first_name,last_name=last_name,email=email,password=password)
            user.save()
            register = Register(user=user,phone_no=phone_no, age=age,gender=gender,id_proof = id_proof, class1 = class1)
            register.save()
            # f1.save()
            # f2.save()
            # v = f1.save(commit=False)

            # j = f2.save(commit=False)
            # v.save()
            # j.save()
            messages.success(self.request, 'registered successfully')
            return redirect("/login/")
        else:
            messages.warning(self.request,'not registered') 
            return redirect('/')
    def get(self,*args, **kwargs):
        f1 = RegisterForm()
        f2 = ProfileForm()
        context = {
            'f1': f1,
            'f2': f2,
        }
        return render(self.request, 'account/register.html',context)

class Loginview(View):
    def post(self,*args,**kwargs):
        user = authenticate(username = self.request.POST['username'], password = self.request.POST['password'])
        if user is not None:
            login(self.request,user)
            messages.success(self.request, 'logged-in successfully')
            if self.request.user.is_superuser:
                return redirect("/details/")

            if self.request.user.is_active:
                return redirect("/classroom/")

            else:
                messages.warning(self.request,'you are not yet approved please wait for approval')
                return redirect("/login/")
        else:
            messages.warning(self.request, 'invalid credentials')
            return redirect("/login/")

    def get(self,*args, **kwargs):
        form = LoginForm()
        return render(self.request, 'account/login.html',{'form':form})

class Logoutview(View):
    def get(self,request):
        logout(request)
        return redirect("/home/")













@method_decorator(login_required, name = 'dispatch')
class Detailsview(ListView):
    model= Register
    template_name = 'account/details.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["object_list"] = Register.objects.all()
        return context

def approve(request, pk):
    if request.user.is_superuser:
        form = Register.objects.get(id=pk)
        form.approve = True
        form.save()
        return redirect("/details/")

def unapprove(request, pk):
    if request.user.is_superuser:
        form = Register.objects.get(id=pk)
        form.approve = False
        form.save()
        return redirect("/details/")

def redirect_view(request):
    return redirect("/home/")