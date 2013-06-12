from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import Post

def index_view(request):
	list_post = Post.objects.all()
	return render(request, 'index.html', {
		'list_post' : list_post,
	})
	
def post(request, year, mounth, day,  slug):
    match_slug = "%s/%s/%s/%s" % (year, mounth, day, slug)
    
    try:
        post = Post.objects.get(slug=match_slug)
        return render(request, 'post_detail.html', {
            'post' : post,
        })
    except Post.DoesNotExist:
        raise Http404
        
def createuser(request):
    if authenticate(username='usuario', password='password') is not None:
        return HttpResponse("Usuario ya ha sido creado")
    try:
        user = User.objects.create_user('usuario', 'a@b.com', 'password')
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return HttpResponse("Usuario creado")
    except:
        return HttpResponse("No se pudo crear el usuario")