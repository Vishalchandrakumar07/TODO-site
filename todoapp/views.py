from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import todo
from django.contrib.auth.decorators import login_required

# @login_required
def home(request): 
    if request.method == 'POST':
        task = request.POST.get('task')
        new_todo = todo(user=request.user, todo_name=task)
        new_todo.save()

    all_todos = todo.objects.filter(user=request.user)
    context = {
        'todos': all_todos
    }
    return render(request, 'todoapp/todo.html', context)

# def register(request):
#     if request.user.is_authenticated:
#         return redirect('home-page')
#     if request.method == 'POST':
#         username = request.POST.get('username', '').strip()
#         email = request.POST.get('email', '').strip()
#         password = request.POST.get('password', '').strip()
       
#         if len(password) <= 3:
#             messages.error(request, 'Password is too short')
#             return redirect('register')

#         get_all_user_by_username = User.objects.filter(username=username)
#         if get_all_user_by_username:
#             messages.error(request, 'Username already exists')
#             return redirect('register') 
        
#         # Create and save new user
#         new_user = User.objects.create_user(username=username, email=email, password=password)
#         new_user.save()

#         messages.success(request, 'Registration successful! Please log in.')
#         return redirect('loginpage')  # Redirect to login page after successful registration

#     return render(request, 'todoapp/register.html')

# def LogoutView(request):
#     logout(request)
#     return redirect('login')

# def loginpage(request):
#     if request.user.is_authenticated:
#         return redirect('home-page')
#     if request.method == 'POST':
#         username = request.POST.get('uname', '').strip()
#         password = request.POST.get('pass', '').strip()

#         validate_user = authenticate(username=username, password=password)
#         if validate_user is not None:
#             login(request, validate_user)
#             return redirect('home-page')
#         else:
#             messages.error(request, 'User does not exist')
#             return redirect('login')  # Ensure this matches your URL name

#     return render(request, 'todoapp/login.html')  # Handles GET requests properly

# @login_required
# def delete_task(request, id):
#     task = get_object_or_404(todo, id=id)
#     task.delete()
#     return redirect('home-page')

# @login_required
# def update_task(request, id):
#     task = todo.objects.get(user=request.user, id=id)
#     task.status = True
#     task.save()
#     return redirect('home-page')