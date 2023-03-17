from django.shortcuts import render,redirect
# from django.http import HttpResponse
import random
def about(request):
    context = {
        'titulo':'About'
    }
    return render(request,'about.html',context)

def home(request):
    context = {'titulo':'Home'}
    return render(request,'home.html',context)

def password(request):
    if request.method == 'POST':
        characters=list('abcdefghijklmnopqrstuvwxyz')
        generated_password=''
        length=int(request.POST.get('length'))
        if request.POST.get('uppercase'):
          characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        if request.POST.get('special'):
           characters.extend('-_+!@#$%^&*')
        if request.POST.get('numbers'):
           characters.extend('0123456789')

        for x in range(length):
          generated_password+=random.choice(characters)
        context = {'titulo':'Password','password':generated_password}
        return render(request,'password.html',context)
    else:
      return redirect('home')
