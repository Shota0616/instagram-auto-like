from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from app.forms import InstaAutoForm


class IndexView(View, InstaAutoForm):
    #template_name = "app/index.html"
    #login_url = '/account/login/'

    def index(self, request, *args, **kwargs):
        form = InstaAutoForm()
        return render(request, 'app/index.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = InstaAutoForm(request.POST or None)
        return render(request, 'app/index.html', {
            'form': form
        })