from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post

from django.contrib.auth.decorators import login_required
# At the first view of the site, if the user is not signedin/up then he
# cannot view anything data from the site


# login required takes user to the login page(login.html) made in users apps
# the functionality to require the user to login is made in settings.py of
# example_project by adding the lines==>LOGIN_URL = 'login' due to which the
# user is redirected to the page named 'login'(which is defined in the
# views.py of users app)
@login_required
def home(request):
    context ={ 'posts' : Post.objects.all()}
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #the format for the url 
    context_object_name = 'posts'
    ordering = ['-date_posted'] #for giving latest post first


# class based view
class PostDetailView(DetailView):
    model = Post

@login_required
def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
