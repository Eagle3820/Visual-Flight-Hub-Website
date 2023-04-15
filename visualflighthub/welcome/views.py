# welcome/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        # User is logged in, show the main page
        return render(request, 'home.html')
    else:
        # User is not logged in, check if they have seen the welcome page before
        if request.session.get('has_seen_welcome', False):
            # User has seen the welcome page before, redirect to login page
            return redirect('login')
        else:
            # User has not seen the welcome page, show it to them and set session variable
            request.session['has_seen_welcome'] = True
            return render(request, 'welcome.html')
