# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from .models import Post
from .forms import PostForm
def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Success")
		return HttpResponseRedirect( instance.get_absolute_url())
	else:
		messages.error(request,"Not Success")
	context = {
	    "form": form,
	}
	return render(request,"post_form.html",context)


def post_update(request,id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Success")
		return HttpResponseRedirect( instance.get_absolute_url())
	context = {
	"title":instance.title,
	'instance': instance,
	    "form": form,
	}
	return render(request,"post_form.html",context)	

def post_delete(request,id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request,"Success Deleted")
	return redirect("list")

def post_list(request):
	queryset_list= Post.objects.all().order_by("-timestamp")
	
	query= request.GET.get('q')
	print ("hi XXXXXXXXXXXXXXXXXXXX ")
	print(query)
	if query:
		queryset_list = queryset_list.filter(title__icontains=query) 
		print(queryset_list)
		print(len(queryset_list))
	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page		
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(	paginator.num_pages)	
	context = {
	"title":"list",
	"object_list":queryset,
	}
	return render(request,"post_list.html",context)





def post_detail(request,id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
	"title":"details",
	'instance': instance,
	}
	return render(request,"post_detail.html",context)		