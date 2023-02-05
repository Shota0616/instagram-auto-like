from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import View
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from app.forms import InstaAutoForm

import logging
logger = logging.getLogger('development')


class IndexView(TemplateView):
    template_name = "app/index.html"

class AutoLikeView(FormView):
    template_name = 'app/app.html'
    form_class = InstaAutoForm

    def form_valid(self, form):
        return render(self.request, 'app/app.html', {'form': form})

class AutoLikeConfirmView(FormView):
    template_name = 'app/confirm.html'
    form_class = InstaAutoForm

    def form_valid(self, form):
        return render(self.request, 'app/confirm.html', {'form': form})