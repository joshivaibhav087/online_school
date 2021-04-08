from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Admin
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout  
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib import messages
from .forms import AddForm
from django.views.generic import ListView, DetailView
from account.models import Register

# Create your views here.

class Addview(View):
    def post(self,*args, **kwargs):
        form = AddForm(self.request.POST,self.request.FILES)
        if form.is_valid():
            class1 = form.cleaned_data['class1']
            subject = form.cleaned_data['subject']
            chapter = form.cleaned_data['chapter']
            video = form.cleaned_data['video']
            notes = form.cleaned_data['notes']

            obj = Admin(user = self.request.user, class1=class1, subject=subject, chapter=chapter, video=video, notes=notes)
            obj.save()

            messages.success(self.request, "chapter added successfully")
            return redirect('/add/')
        else:
            messages.warning(self.request,"invalid data")
            return redirect("/add/")

    def get(self,*args, **kwargs):
        form = AddForm()
        return render(self.request, "admin/add.html", {'form':form})
        
# class Classview(ListView):
#     model = Admin
#     template_name = "student/student.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["object_list"] = Admin.objects.all()
#         return context
class Classview(View):
    model = Admin
    template_name = "student/student.html"

    def get(self, *args, **kwargs):
        try:
            register = Register.objects.get(approve=True, user=self.request.user)
            if register:
                object_list= Admin.objects.all()
                return render(self.request, 'student/student.html',{'object_list':object_list})
        except:
            messages.warning(self.request, "please wait for approval")
            return redirect("/login/")
            
class Dview(DetailView):
    model = Admin
    template_name = "student/more.html"  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["object_list"] = Admin.objects.all()
        return context

