from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import View
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from app.forms import InstaAutoForm

import logging
logger = logging.getLogger(__name__)

# app = Celery('tasks', backend='amqp', broker='amqp://admin:admin@127.0.0.1:5672')

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

    """
    以下インスタグラムいいね自動実行の関数
    """
    def main(self, form):
        # 変数
        email = form.cleaned_data['insta_email']
        password = form.cleaned_data['insta_password']
        num_of_times = form.cleaned_data['insta_num_of_times']
        # 他の変数（後でformから入力可能にするかも）
        tags = ['バイク', 'ドラッグスター']

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        wait = WebDriverWait(driver=driver, timeout=30)

        # ログイン実行
        insta_login(email, password, driver)
        # タグ検索用urlセット（リストで取得）
        tagurllist = tagsearch(tags, driver)

    """
    ログイン
    """
    def insta_login(self, email, password, driver):
        # 変数
        submit_btn = '_acan'

        # urlを開く
        driver.get(https://www.instagram.com/)
        # 要素がすべて抽出できるまで待機
        wait.until(EC.presence_of_all_elements_located)
        # メールアドレスとパスワードを入力，及びログイン
        driver.find_element_by_name('username').send_keys(username)
        time.sleep(1)
        driver.find_element_by_name('password').send_keys(password)
        time.sleep(1)
        driver.find_element_by_class_name(submit_btn)
        wait.until(EC.presence_of_all_elements_located)

    def tagsearch(self, tags, driver)
        # 変数
        tagsearchurl = 'https://www.instagram.com/explore/tags/'
        tagurllist = []
        # tagが複数ある場合は分割
        for tag in tags:
            tagurllist.append(tagsearchurl + tag)

        return tagurllist

    def like()
