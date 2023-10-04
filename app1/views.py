from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.contrib import messages

# this function will add new items and show items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # fm.save()
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
            messages.success(request, "Student successfully created!")

    else:
        fm = StudentRegistration()
        
    stud = User.objects.all()        
    return render(request, 'app1/addshow.html', {'form': fm, 'stu': stud})

# this will update/Edit
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save
                    
        messages.success(request, "Student successfully Updated!")

    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        
    return render(request, 'app1/update.html', {'form': fm})


# this will delete items
def delete_data(request, id):
    # if request.method == 'POST':
    de = User.objects.get(pk=id)
    de.delete()
                
    messages.success(request, "Student Deleted successfully!")
    
    return HttpResponseRedirect('/')
        
        