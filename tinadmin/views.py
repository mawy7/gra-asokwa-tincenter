from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
#...

def staff_only(function):
    """
    Custom view decorator allows us to raise 403 on insufficient permissions,
    rather than redirect user to login view.
    """
    def wrap(request, *args, **kwargs):
        if request.user.is_staff:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

@staff_only
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Account created successfully')
			return redirect('register')

	else:
		form = UserCreationForm()
	token = {}
	token.update(csrf(request))
	token['form'] = form

	return render_to_response('register.html', token) 