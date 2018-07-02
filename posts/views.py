# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

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
	queryset= Post.objects.all()
	context = {
	"title":"list",
	"object_list":queryset,
	}
	return render(request,"index.html",context)
def post_detail(request,id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
	"title":"details",
	'instance': instance,
	}
	return render(request,"post_detail.html",context)		