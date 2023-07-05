```python
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username, password=password)
        user.save()
        return HttpResponse("User registered successfully")
    else:
        return HttpResponse("Invalid request")

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("User logged in successfully")
        else:
            return HttpResponse("Invalid credentials")
    else:
        return HttpResponse("Invalid request")

def logout_view(request):
    logout(request)
    return HttpResponse("User logged out successfully")
```