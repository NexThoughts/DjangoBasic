from django.shortcuts import render
import forms


import datetime

def currentDate(request):
    loginForm=forms.loginform(request.POST or None)
    if(loginForm.is_valid()):
        print('great')
    else:
        print(loginForm.errors)
        current=datetime.datetime.now()
        names=['amti','divyansh','kshitij']
        return render(request,'date.html',{'currentDate':current,'names':names,'form':loginForm})