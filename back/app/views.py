from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import View
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep

from app.forms import InstaAutoForm

import logging
logger = logging.getLogger(__name__)

# app = Celery('tasks', backend='amqp', broker='amqp://admin:admin@127.0.0.1:5672')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install())

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
        # email = form.cleaned_data['insta_email']
        # password = form.cleaned_data['insta_password']
        # num_of_times = form.cleaned_data['insta_num_of_times']
        auto_like(form)
        return render(self.request, 'app/confirm.html', {'form': form})


    # 自動実行関数
    def auto_like(self, form):
        # formから取得した値を変数に格納
        email = form.cleaned_data['insta_email']
        password = form.cleaned_data['insta_password']
        num_of_times = form.cleaned_data['insta_num_of_times']

        # 処理
        driver.get('https://google.com')