from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.base import TemplateView

from utils.decorators import LoginRequiredMixin

class HomeView(LoginRequiredMixin, TemplateView):
	template_name = 'core/home.html' 

class AboutView(TemplateView):
	template_name = 'core/about.html'