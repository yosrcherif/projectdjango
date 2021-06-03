from todolist.models import User, UserDetails
from django.shortcuts import render,redirect
from .forms import *
# Create your views here.
def login(request):
    if request.session.has_key('todoId'):
        return redirect('home')
    else:
        if request.method =='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.filter(username = username,password = password).first()
            if user:
                request.session['todoId'] = user.id
                return redirect('home')
            else:
                msg = "Username or password incorrect"
                return render(request,'login.html',{'message':msg})
    return render(request,'login.html',{})

def register(request):
    if request.session.has_key('todoId'):
        return  redirect('home')
    else:
        if request.method == 'POST':
            det = UserDetails()
            user = User()
            det.name = request.POST['name']
            det.prenom = request.POST['prenom']
            det.save()
            user.username = request.POST['username']
            user.password = request.POST['password']
            user.details = det
            user.save()
            request.session['todoId'] = user.id
            return redirect('home')
    return render(request,'register.html',{})
def logout(request):
    if not request.session.has_key('todoId'):
        return redirect('login')
    try:
        del request.session['todoId']
        return redirect('login')
    except:
        pass

def home(request):
    if request.session.has_key('todoId'):
        user = User.objects.filter(id = request.session['todoId']).first()
        return render(request,'home.html',{'user':user})
    else:
        return redirect('login')

def addtodo(request):
    if request.session.has_key('todoId'):
        user = User.objects.filter(id = request.session['todoId']).first()
        if request.method == 'POST':
            form = todo()
            form.title = request.POST['title']
            form.descr = request.POST['descr']
            form.save()
            user.todolist.add(form)
            return redirect('home')
        else:
            form = TodoForm()
            return render(request,'addtodo.html',{'form':form})
    else:
        return redirect('login')

def deletetodo(request,id):
    if request.session.has_key('todoId'):
        td = todo.objects.filter(id = id).first()
        td.delete()
        return  redirect('home')
    else:
        return redirect('login')

def checktodo(request,id):
    if request.session.has_key('todoId'):
        td = todo.objects.filter(id = id).first()
        td.cmpte = True
        td.save(update_fields=['cmpte'])
        return  redirect('home')
    else:
        return redirect('login')

def edittodo(request,id):
    if request.session.has_key('todoId'):
        td = todo.objects.filter(id = id).first()
        if request.method == "POST":
            td.title = request.POST['title']
            td.descr = request.POST['descr']
            cmpte = request.POST.getlist('cmpte')
            if len(cmpte):

                td.cmpte = True
            else:
                td.cmpte = False

            td.save(update_fields=['title','descr','cmpte'])
            return redirect('home')
        else:
            return render(request,'edit.html',{'todo':td})
    else:
        return redirect('login')
        