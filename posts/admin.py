# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
	list_display =["title","timestamp","updated"]
	list_display_links=["updated"]
	# list_display_link=["updated"]
	list_filter =["updated","timestamp"]
	list_editable=["title"]
	class Meta:
		model=Post


admin.site.register(Post, PostModelAdmin)