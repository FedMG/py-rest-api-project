from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature


def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email,
                                                password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password is not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None: # user
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def post(request, pk):
    return render(request, 'post.html', { 'pk': pk })


def counter(request):
    posts = [1,2,3,4, 'john', 'admin']
    return render(request, 'counter.html', {'posts': posts })



# def counter(request):
#     # 'text' is the keyword name attribute value in the input form
#     # text = request.GET['text']
#     text = request.POST['text']
#     amount_of_words = len(text.split())
#     return render(request, 'counter.html', {'amount': amount_of_words})    


# from django.http import HttpResponse

# Create your views here.
# def index (request):
#     return HttpResponse('<h1>Hello World!</h1>')

# def index (request):
    # context = {
    #     'name': 'Patrick',
    #     'age': 23
    # }

    # return render(request, 'index.html', context)


# def index(request):
#     feature1 = Feature()
#     feature1.id = 0
#     feature1.name = 'Fast 1'
#     feature1.is_true = True
#     feature1.details = 'Our Service 1'

#     feature2 = Feature()
#     feature2.id = 1
#     feature2.name = 'Fast 2'
#     feature2.is_true = False
#     feature2.details = 'Our Service 2'

#     feature3 = Feature()
#     feature3.id = 2
#     feature3.name = 'Fast 3'
#     feature3.is_true = False
#     feature3.details = 'Our Service 3'

#     features = [feature1, feature2, feature3]

#     return render(request, 'index.html', {'features': features})
