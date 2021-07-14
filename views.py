from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password1']

        x = User.objects.create_user(name=name, email=email, password=password)
        x.save()

        print("User Created.!!!")
        return redirect('index.html')
    else:
        return render(request, '/signup.html')
