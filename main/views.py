from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render , redirect
from django.views.generic import ListView
from .models import Blog, OurServices , Gallery , HomeBg
from .forms import ContactUsForm

class HomeListView(ListView):
    template_name = 'index.html'


    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        blogs = Blog.objects.all()
        services = OurServices.objects.get()
        galleries = Gallery.objects.all()
        backgrounds = HomeBg.objects.get()
        context = {
            'blogs':blogs,
            'services':services,
            'galleries':galleries,
            'backgrounds':backgrounds,
        }

        return render(request, self.template_name , context=context)

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = ContactUsForm()

        return redirect('/')

