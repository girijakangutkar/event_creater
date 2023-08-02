from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from eveapp.forms import UserForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from .models import Event
from django.views import View
from .forms import EventForm
from django.contrib import messages


# Create your views here.


class about(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'eveapp/about.html')
    
    
def EventInfo(request):
    event_info = Event.objects.all()
    context = {
        'event_info' : event_info
    }
    return render(request, 'eveapp/eventinfo.html', context)

    

def eventpage(request):
  if request.method == "POST":
    Event_form = EventForm(request.POST, request.FILES)
    if Event_form.is_valid():
      Event_form.save()
      messages.success(request, ('Your Event was successfully added!'))
    else:
	    messages.error(request, 'Error saving form')
    return redirect("EventInfo")
  Event_form = EventForm()
  events = Event.objects.all()
  return render(request=request, template_name="eveapp/event.html", context={'Event_form':Event_form, 'events':events})


@login_required
def special(request):
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse_lazy('EventInfo'))

def SignUp(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        

    # This is the render and context dictionary to feed
    return render(request,'eveapp/signup.html',
                          {'user_form':user_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse_lazy('eventpage'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'eveapp/login.html', {})
