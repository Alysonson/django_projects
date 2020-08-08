from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
    model = Post # qual o modelo se refere
    template_name = 'home.html' # qual o template se refere
    context_object_name = 'all_posts_list' # o nome que o template ira usar para referenciar essa classe