from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.conf.urls import include
from health.models import Staff

def recephome(request):
    context_dict = {}
    response = render(request, 'health/recephome.html', context_dict)

    return response

def adminhome(request):
    context_dict = {}
    response = render(request, 'health/adminhome.html', context_dict)

    return response

def dochome(request):
    context_dict = {}
    response = render(request, 'health/dochome.html', context_dict)

    return response

def labhome(request):
    context_dict = {}
    response = render(request, 'health/labhome.html', context_dict)

    return response

def patienthome(request):
    context_dict = {}
    response = render(request, 'health/patienthome.html', context_dict)

    return response

def user_login(request):
# If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
# Gather the username and password provided by the user.
# This information is obtained from the login form.
# We use request.POST.get('<variable>') as opposed
# to request.POST['<variable>'], because the
# request.POST.get('<variable>') returns None if the
# value does not exist, while request.POST['<variable>']
# will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')

# Use Django's machinery to attempt to see if the username/password
# combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

# If we have a User object, the details are correct.
# If None (Python's way of representing the absence of a value), no user
# with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
                if user.is_active:
                    if user.user_type == 1:
# If the account is valid and active, we can log the user in.
# We'll send the user back to the homepage.
                        login(request, user)
                        return render(request, 'health/dochome.html', {})
                    elif user.user_type == 2:
                        login(request, user)
                        return render(request, 'health/labhome.html', {})
                    elif user.user_type == 3:
                        login(request, user)
                        return render(request, 'health/recephome.html', {})
                    elif user.user_type == 4:
                        login(request, user)
                        return render(request, 'health/patienthome.html', {})
                    elif user.user_type == 5:
                        login(request, user)
                        return render(request, 'health/adminhome.html', {})
                else:
# An inactive account was used - no logging in!
                    return HttpResponse("Your Rango account is disabled.")
        else:
# Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
# The request is not a HTTP POST, so display the login form.
# This scenario would most likely be a HTTP GET.
    else:
# No context variables to pass to the template system, hence the # blank dictionary object...
        return render(request, 'rango/login.html', {})
