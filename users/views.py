from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# if user is not signedup/in the he cannot see the profile of any user
# on the site
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
#UserUpdateForm, ProfileUpdateForm for the profile method

def register(request):
    if request.method == 'POST': #if we get a post request then we will validate
    #the form data
        form = UserRegistrationForm(request.POST) #if we get a post request then
        #create a form using the data that was in Post
        #this line also saves the data on the username field even if the form inavlidates

        if form.is_valid():
            form.save() #saves the user if  the form is valid
            username = form.cleaned_data.get('username')#validated username data will
            #be in cleaned_data dictionary
            messages.success(request, f'Your account has been created! You are now able to login')
            #Flash message #f string used
            return redirect('login')#redirecting to login page if form is valid
        # if the form is invalid then django automatically displays the error messages
        # with the specific error

    else: #if get request then we will redirect to the registration form again
        form = UserRegistrationForm()#creates an empty form
    return render(request, 'users/register.html',{'form':form})


# login required takes user to the login page(login.html) made in users apps
# the functionality to require the user to login is made in settings.py of
# example_project by adding the lines==>LOGIN_URL = 'login' due to which the
# user is redirected to the page named 'login'(which is defined in the
# views.py of users app)

# login_required decorator is put so that in the logged out state the user wont be
# able to access the profile page
@login_required
def profile(request):
    # we will need to put in a check to see if it is a post route
    # If it is a post route then we will have to check if the form is valid
    # If the form is valid the will save that information
    if request.method == 'POST':
        u_form= UserUpdateForm(request.POST, instance=request.user)
        # instance=request.username==>populating the username from the UserUpdateForm
        p_form= ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        # A view handling this form will receive the file data in request.FILES,
        # which is a dictionary containing a key for each FileField
        # (or ImageField, or other FileField subclass) in the form.
        # So the data from the above form would be accessible as
        # request.FILES['file'].
        # Note that request.FILES will only contain data if the request method
        # was POST and the <form> that posted the request has the attribute
        # enctype="multipart/form-data". Otherwise, request.FILES will be empty.
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form= UserUpdateForm(instance=request.user)
        # instance=request.username==>populating the username from the UserUpdateForm
        p_form= ProfileUpdateForm(instance=request.user.profile)
    # instance=request.profile==>populating the image of current user

    context={
        'u_form' : u_form,
        'p_form' : p_form,
    }
    return render(request, 'users/profile.html', context)
