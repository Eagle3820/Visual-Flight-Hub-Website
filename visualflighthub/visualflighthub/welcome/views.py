# welcome/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# checks if user has seen welcome
def welcome(request):
    # User is not logged in, check if they have seen the welcome page before
    if request.session.get('has_seen_welcome', True):
        # User has seen the welcome page before, redirect to login page
        return redirect('home')
    else:
        # User has not seen the welcome page, show it to them and set session variable
        request.session['has_seen_welcome'] = True
        return render(request, 'welcome.html')

def reset_session(request):
    if 'has_seen_welcome' in request.session:
        del request.session['has_seen_welcome']
    return redirect('home')

# redirect to home page
def home(request):
    return render(request, 'home.html')